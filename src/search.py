from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)
from langchain_core.messages import trim_messages
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda, RunnableWithMessageHistory
from dotenv import load_dotenv

load_dotenv()

PROMPT_TEMPLATE = """
CONTEXTO:
{contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{pergunta}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""

session_store: dict[str, InMemoryChatMessageHistory] = {}


def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]


def prepare_inputs(payload: dict) -> dict:
    raw_history = payload.get("raw_history", [])
    trimmed = trim_messages(
        raw_history,
        token_counter=len,
        max_tokens=10,
        strategy="last",
        start_on="system",
        include_system=True,
        allow_partial=False,
    )

    return {
        "pergunta": payload.get("pergunta", ""),
        "contexto": payload.get("contexto", ""),
        "history": trimmed,
    }


def search_prompt():
    chat_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", PROMPT_TEMPLATE),
            MessagesPlaceholder(variable_name="history"),
        ],
    )

    llm = ChatOpenAI(model="gpt-5-nano", temperature=0.5)

    prepare = RunnableLambda(prepare_inputs)

    chain = prepare | chat_prompt | llm

    conversational_chain = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="pergunta",
        history_messages_key="raw_history",
    )

    return conversational_chain
