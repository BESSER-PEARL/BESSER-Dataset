





import java.util.List;
import java.util.ArrayList;

public class arithmetics_Import  {

    private String importedNamespace;





    private arithmetics_Module arithmetics_module;


    public arithmetics_Import(
        String importedNamespace    ) {
        this.importedNamespace = importedNamespace;
    }


    public String getImportednamespace() {
        return importedNamespace;
    }

    public void setImportednamespace(String importedNamespace) {
        this.importedNamespace = importedNamespace;
    }

    public arithmetics_Module getArithmetics_module() {
        return arithmetics_module;
    }

    public void setArithmetics_module(arithmetics_Module arithmetics_module) {
        this.arithmetics_module = arithmetics_module;
    }

}