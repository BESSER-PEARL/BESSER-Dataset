





import java.util.List;
import java.util.ArrayList;

public class wh_Import extends AbstractElement {

    private String importedNamespace;



    public wh_Import(
        String importedNamespace    ) {
        super(
        );
        this.importedNamespace = importedNamespace;
    }


    public String getImportednamespace() {
        return importedNamespace;
    }

    public void setImportednamespace(String importedNamespace) {
        this.importedNamespace = importedNamespace;
    }


}