





import java.util.List;
import java.util.ArrayList;

public class blorqueScript_BSImport  {

    private String importedNamespace;





    private blorqueScript_BSFile blorquescript_bsfile;


    public blorqueScript_BSImport(
        String importedNamespace    ) {
        this.importedNamespace = importedNamespace;
    }


    public String getImportednamespace() {
        return importedNamespace;
    }

    public void setImportednamespace(String importedNamespace) {
        this.importedNamespace = importedNamespace;
    }

    public blorqueScript_BSFile getBlorquescript_bsfile() {
        return blorquescript_bsfile;
    }

    public void setBlorquescript_bsfile(blorqueScript_BSFile blorquescript_bsfile) {
        this.blorquescript_bsfile = blorquescript_bsfile;
    }

}