





import java.util.List;
import java.util.ArrayList;

public class soa_Import  {

    private String importedNamespace;





    private soa_Module soa_module;


    public soa_Import(
        String importedNamespace    ) {
        this.importedNamespace = importedNamespace;
    }


    public String getImportednamespace() {
        return importedNamespace;
    }

    public void setImportednamespace(String importedNamespace) {
        this.importedNamespace = importedNamespace;
    }

    public soa_Module getSoa_module() {
        return soa_module;
    }

    public void setSoa_module(soa_Module soa_module) {
        this.soa_module = soa_module;
    }

}