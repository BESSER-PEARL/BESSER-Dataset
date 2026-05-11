





import java.util.List;
import java.util.ArrayList;

public class ir_Import extends IrAnnotable {

    private String importedNamespace;



    public ir_Import(
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