





import java.util.List;
import java.util.ArrayList;

public class nabla_Import  {

    private String importedNamespace;





    private nabla_NablaModule nabla_nablamodule;


    public nabla_Import(
        String importedNamespace    ) {
        this.importedNamespace = importedNamespace;
    }


    public String getImportednamespace() {
        return importedNamespace;
    }

    public void setImportednamespace(String importedNamespace) {
        this.importedNamespace = importedNamespace;
    }

    public nabla_NablaModule getNabla_nablamodule() {
        return nabla_nablamodule;
    }

    public void setNabla_nablamodule(nabla_NablaModule nabla_nablamodule) {
        this.nabla_nablamodule = nabla_nablamodule;
    }

}