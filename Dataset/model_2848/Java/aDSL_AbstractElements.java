





import java.util.List;
import java.util.ArrayList;

public class aDSL_AbstractElements  {

    private String importedNamespace;





    private aDSL_Program adsl_program;


    public aDSL_AbstractElements(
        String importedNamespace    ) {
        this.importedNamespace = importedNamespace;
    }


    public String getImportednamespace() {
        return importedNamespace;
    }

    public void setImportednamespace(String importedNamespace) {
        this.importedNamespace = importedNamespace;
    }

    public aDSL_Program getAdsl_program() {
        return adsl_program;
    }

    public void setAdsl_program(aDSL_Program adsl_program) {
        this.adsl_program = adsl_program;
    }

}