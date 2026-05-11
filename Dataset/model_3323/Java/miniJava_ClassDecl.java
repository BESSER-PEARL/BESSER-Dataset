





import java.util.List;
import java.util.ArrayList;

public class miniJava_ClassDecl  {

    private String name;





    private miniJava_Program minijava_program;




    private miniJava_ClassDecl minijava_classdecl;


    public miniJava_ClassDecl(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public miniJava_Program getMinijava_program() {
        return minijava_program;
    }

    public void setMinijava_program(miniJava_Program minijava_program) {
        this.minijava_program = minijava_program;
    }
    public miniJava_ClassDecl getMinijava_classdecl() {
        return minijava_classdecl;
    }

    public void setMinijava_classdecl(miniJava_ClassDecl minijava_classdecl) {
        this.minijava_classdecl = minijava_classdecl;
    }

}