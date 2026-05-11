





import java.util.List;
import java.util.ArrayList;

public class domainmodel_Import extends AbstractNamespaceElement {

    private String importedNamespace;



    public domainmodel_Import(
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