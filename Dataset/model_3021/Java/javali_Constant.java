





import java.util.List;
import java.util.ArrayList;

public class javali_Constant  {

    private boolean static;





    private javali_Module javali_module;




    private javali_Identifier javali_identifier;




    private javali_Literal javali_literal;




    private javali_Type javali_type;


    public javali_Constant(
        boolean static    ) {
        this.static = static;
    }


    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }

    public javali_Module getJavali_module() {
        return javali_module;
    }

    public void setJavali_module(javali_Module javali_module) {
        this.javali_module = javali_module;
    }
    public javali_Identifier getJavali_identifier() {
        return javali_identifier;
    }

    public void setJavali_identifier(javali_Identifier javali_identifier) {
        this.javali_identifier = javali_identifier;
    }
    public javali_Literal getJavali_literal() {
        return javali_literal;
    }

    public void setJavali_literal(javali_Literal javali_literal) {
        this.javali_literal = javali_literal;
    }
    public javali_Type getJavali_type() {
        return javali_type;
    }

    public void setJavali_type(javali_Type javali_type) {
        this.javali_type = javali_type;
    }

}