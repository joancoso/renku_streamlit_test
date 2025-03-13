# Configuration file for jupyter-notebook.

c.ServerProxy.servers = {
    'streamlit': {
        'command': [
            'streamlit',
            'run',
            'work/streamlit-v2-example/helloworld.py',
            '--server.port', '8501',
            '--browser.serverAddress', '0.0.0.0',
            '--server.runOnSave', '1',
            '--server.allowRunOnSave', '1'
        ],
        'port': 8501,
        'timeout': 60
    }
}
