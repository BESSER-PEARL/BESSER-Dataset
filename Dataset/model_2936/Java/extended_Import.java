





import java.util.List;
import java.util.ArrayList;

public class extended_Import extends AbstractElement {

    private String importedNamespace;



    public extended_Import(
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