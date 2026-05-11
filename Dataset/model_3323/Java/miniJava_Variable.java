





import java.util.List;
import java.util.ArrayList;

public class miniJava_Variable  {

    private String name;





    private miniJava_Type minijava_type;




    private miniJava_VarDeclaration minijava_vardeclaration;




    private miniJava_Statement minijava_statement;




    private miniJava_Method minijava_method;


    public miniJava_Variable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public miniJava_Type getMinijava_type() {
        return minijava_type;
    }

    public void setMinijava_type(miniJava_Type minijava_type) {
        this.minijava_type = minijava_type;
    }
    public miniJava_VarDeclaration getMinijava_vardeclaration() {
        return minijava_vardeclaration;
    }

    public void setMinijava_vardeclaration(miniJava_VarDeclaration minijava_vardeclaration) {
        this.minijava_vardeclaration = minijava_vardeclaration;
    }
    public miniJava_Statement getMinijava_statement() {
        return minijava_statement;
    }

    public void setMinijava_statement(miniJava_Statement minijava_statement) {
        this.minijava_statement = minijava_statement;
    }
    public miniJava_Method getMinijava_method() {
        return minijava_method;
    }

    public void setMinijava_method(miniJava_Method minijava_method) {
        this.minijava_method = minijava_method;
    }

}