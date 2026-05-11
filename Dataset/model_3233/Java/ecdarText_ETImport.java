





import java.util.List;
import java.util.ArrayList;

public class ecdarText_ETImport  {

    private String importedNamespace;





    private ecdarText_ETFile ecdartext_etfile;


    public ecdarText_ETImport(
        String importedNamespace    ) {
        this.importedNamespace = importedNamespace;
    }


    public String getImportednamespace() {
        return importedNamespace;
    }

    public void setImportednamespace(String importedNamespace) {
        this.importedNamespace = importedNamespace;
    }

    public ecdarText_ETFile getEcdartext_etfile() {
        return ecdartext_etfile;
    }

    public void setEcdartext_etfile(ecdarText_ETFile ecdartext_etfile) {
        this.ecdartext_etfile = ecdartext_etfile;
    }

}