import polib

def compile_mo(file_path):
    po = polib.pofile(file_path)
    mo_path = file_path.replace('.po', '.mo')
    po.save_as_mofile(mo_path)
    print(f"Compiled {file_path} to {mo_path}")

# Türkçe ve İngilizce .po dosyalarını .mo dosyalarına dönüştürme
compile_mo('locale/en/LC_MESSAGES/messages.po')
compile_mo('locale/tr/LC_MESSAGES/messages.po')
