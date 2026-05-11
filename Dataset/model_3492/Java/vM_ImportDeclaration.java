





import java.util.List;
import java.util.ArrayList;

public class vM_ImportDeclaration extends VmBlock {

    private String importedNamespace;



    public vM_ImportDeclaration(
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