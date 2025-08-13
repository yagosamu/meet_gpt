# Dicionários simples de i18n para UI e prompts de resumo
LANG = {
    "pt": {
        "ui": {
            "app_title": "Bem-vindo ao MeetGPT 🎙️",
            "tab_record": "Gravar Reunião",
            "tab_saved": "Ver transcrições salvas",
            "start_talking": "Comece a falar",
            "select_meeting": "Selecione uma reunião",
            "add_title": "Adicione um título",
            "meeting_title": "Título da reunião",
            "save": "Salvar",
            "transcription_label": "Transcrição:",
            "summary_label": "Resumo:",
            "transcription_language": "Idioma da transcrição",
            "summary_language": "Idioma do resumo",
            "auto": "Automático",
        },
        "prompt": """Faça o resumo do texto delimitado por ####.
O texto é a transcrição de uma reunião. O resumo deve contar os principais assuntos abordados.
O resumo deve ter no máximo 300 caracteres e estar em texto corrido.
No final, apresente todos os acordos e combinados em bullet points.
Formato final:
Resumo da reunião:
- escreva aqui o resumo.
Acordos da reunião:
- acordo 1
- acordo 2
- acordo n
texto:
####{}####"""
    },
    "en": {
        "ui": {
            "app_title": "Welcome to MeetGPT 🎙️",
            "tab_record": "Record Meeting",
            "tab_saved": "Saved Transcriptions",
            "start_talking": "Start speaking",
            "select_meeting": "Select a meeting",
            "add_title": "Add a title",
            "meeting_title": "Meeting title",
            "save": "Save",
            "transcription_label": "Transcription:",
            "summary_label": "Summary:",
            "transcription_language": "Transcription language",
            "summary_language": "Summary language",
            "auto": "Auto",
        },
        "prompt": """Summarize the text delimited by ####.
The text is a meeting transcription. The summary must capture the main topics discussed.
The summary must be a single paragraph with at most 300 characters.
At the end, list all agreements and action items as bullet points.
Final format:
Meeting summary:
- write the summary here.
Meeting agreements:
- agreement 1
- agreement 2
- agreement n
text:
####{}####"""
    }
}