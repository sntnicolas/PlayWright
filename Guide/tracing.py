context = browser.new_context()
context.tracing.start(screenshots=True, snapshots=True, sources=True)

# ... действия/тесты ...

context.tracing.stop(path="trace.zip")  # откроешь в Playwright Trace Viewer

# Ещё инструменты:
#
# Inspector: PWDEBUG=1 (в Windows PowerShell: $env:PWDEBUG=1; python run.py) — пошаговая отладка с подсветкой локаторов.
# codegen: записывает действия в код
# playwright codegen https://example.com --target python