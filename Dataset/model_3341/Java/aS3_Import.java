





import java.util.List;
import java.util.ArrayList;

public class aS3_Import  {

    private String importedNamespace;





    private aS3_Imports as3_imports;


    public aS3_Import(
        String importedNamespace    ) {
        this.importedNamespace = importedNamespace;
    }


    public String getImportednamespace() {
        return importedNamespace;
    }

    public void setImportednamespace(String importedNamespace) {
        this.importedNamespace = importedNamespace;
    }

    public aS3_Imports getAs3_imports() {
        return as3_imports;
    }

    public void setAs3_imports(aS3_Imports as3_imports) {
        this.as3_imports = as3_imports;
    }

}