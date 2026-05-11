





import java.util.List;
import java.util.ArrayList;

public class miniJava_Import  {

    private String importedNamespace;





    private miniJava_Program minijava_program;


    public miniJava_Import(
        String importedNamespace    ) {
        this.importedNamespace = importedNamespace;
    }


    public String getImportednamespace() {
        return importedNamespace;
    }

    public void setImportednamespace(String importedNamespace) {
        this.importedNamespace = importedNamespace;
    }

    public miniJava_Program getMinijava_program() {
        return minijava_program;
    }

    public void setMinijava_program(miniJava_Program minijava_program) {
        this.minijava_program = minijava_program;
    }

}