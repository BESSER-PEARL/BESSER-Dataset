





import java.util.List;
import java.util.ArrayList;

public class miniJava_TypeDeclaration extends NamedElement {

    private String accessLevel;





    private miniJava_Program minijava_program;


    public miniJava_TypeDeclaration(
        String accessLevel    ) {
        super(
        );
        this.accessLevel = accessLevel;
    }


    public String getAccesslevel() {
        return accessLevel;
    }

    public void setAccesslevel(String accessLevel) {
        this.accessLevel = accessLevel;
    }

    public miniJava_Program getMinijava_program() {
        return minijava_program;
    }

    public void setMinijava_program(miniJava_Program minijava_program) {
        this.minijava_program = minijava_program;
    }

}