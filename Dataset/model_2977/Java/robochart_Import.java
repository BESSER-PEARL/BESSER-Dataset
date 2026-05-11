





import java.util.List;
import java.util.ArrayList;

public class robochart_Import  {

    private String importedNamespace;





    private robochart_BasicPackage robochart_basicpackage;


    public robochart_Import(
        String importedNamespace    ) {
        this.importedNamespace = importedNamespace;
    }


    public String getImportednamespace() {
        return importedNamespace;
    }

    public void setImportednamespace(String importedNamespace) {
        this.importedNamespace = importedNamespace;
    }

    public robochart_BasicPackage getRobochart_basicpackage() {
        return robochart_basicpackage;
    }

    public void setRobochart_basicpackage(robochart_BasicPackage robochart_basicpackage) {
        this.robochart_basicpackage = robochart_basicpackage;
    }

}