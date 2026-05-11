





import java.util.List;
import java.util.ArrayList;

public class javali_Procedure  {

    private boolean static;
    private boolean void;
    private String comment;





    private javali_Identifier javali_identifier;




    private javali_Module javali_module;




    private javali_Block javali_block;




    private List<javali_VarDeclaration> javali_vardeclarations;




    private javali_Type javali_type;


    public javali_Procedure(
        boolean static,        boolean void,        String comment    ) {
        this.static = static;
        this.void = void;
        this.comment = comment;
        this.javali_vardeclarations = new ArrayList<>();
    }

    public javali_Procedure(
        boolean static,        boolean void,        String comment        ArrayList<javali_VarDeclaration> javali_vardeclarations    ) {
        this.static = static;
        this.void = void;
        this.comment = comment;
        this.javali_vardeclarations = javali_vardeclarations;
    }

    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public boolean getVoid() {
        return void;
    }

    public void setVoid(boolean void) {
        this.void = void;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public javali_Identifier getJavali_identifier() {
        return javali_identifier;
    }

    public void setJavali_identifier(javali_Identifier javali_identifier) {
        this.javali_identifier = javali_identifier;
    }
    public javali_Module getJavali_module() {
        return javali_module;
    }

    public void setJavali_module(javali_Module javali_module) {
        this.javali_module = javali_module;
    }
    public javali_Block getJavali_block() {
        return javali_block;
    }

    public void setJavali_block(javali_Block javali_block) {
        this.javali_block = javali_block;
    }
    public List<javali_VarDeclaration> getJavali_vardeclarations() {
        return javali_vardeclarations;
    }

    public void addJavali_vardeclaration(Javali_vardeclaration javali_vardeclaration) {
        this.javali_vardeclarations.add(javali_vardeclaration);
    }
    public javali_Type getJavali_type() {
        return javali_type;
    }

    public void setJavali_type(javali_Type javali_type) {
        this.javali_type = javali_type;
    }

}