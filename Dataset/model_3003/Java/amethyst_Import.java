





import java.util.List;
import java.util.ArrayList;

public class amethyst_Import  {

    private String importedNamespace;





    private amethyst_Module amethyst_module;


    public amethyst_Import(
        String importedNamespace    ) {
        this.importedNamespace = importedNamespace;
    }


    public String getImportednamespace() {
        return importedNamespace;
    }

    public void setImportednamespace(String importedNamespace) {
        this.importedNamespace = importedNamespace;
    }

    public amethyst_Module getAmethyst_module() {
        return amethyst_module;
    }

    public void setAmethyst_module(amethyst_Module amethyst_module) {
        this.amethyst_module = amethyst_module;
    }

}