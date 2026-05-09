





import java.util.List;
import java.util.ArrayList;

public class vhdl_UseClause extends ContextItem {

    private String importedNamespace;



    public vhdl_UseClause(
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