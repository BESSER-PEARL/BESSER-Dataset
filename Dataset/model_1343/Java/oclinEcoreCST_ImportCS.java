





import java.util.List;
import java.util.ArrayList;

public class oclinEcoreCST_ImportCS  {

    private String importedNamespace;





    private oclinEcoreCST_DocumentCS oclinecorecst_documentcs;


    public oclinEcoreCST_ImportCS(
        String importedNamespace    ) {
        this.importedNamespace = importedNamespace;
    }


    public String getImportednamespace() {
        return importedNamespace;
    }

    public void setImportednamespace(String importedNamespace) {
        this.importedNamespace = importedNamespace;
    }

    public oclinEcoreCST_DocumentCS getOclinecorecst_documentcs() {
        return oclinecorecst_documentcs;
    }

    public void setOclinecorecst_documentcs(oclinEcoreCST_DocumentCS oclinecorecst_documentcs) {
        this.oclinecorecst_documentcs = oclinecorecst_documentcs;
    }

}