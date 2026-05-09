





import java.util.List;
import java.util.ArrayList;

public class java_VariableDeclaration extends NamedElement {

    private int extraArrayDimensions;





    private java_Expression java_expression;




    private java_SingleVariableAccess java_singlevariableaccess;


    public java_VariableDeclaration(
        int extraArrayDimensions    ) {
        super(
        );
        this.extraArrayDimensions = extraArrayDimensions;
    }


    public int getExtraarraydimensions() {
        return extraArrayDimensions;
    }

    public void setExtraarraydimensions(int extraArrayDimensions) {
        this.extraArrayDimensions = extraArrayDimensions;
    }

    public java_Expression getJava_expression() {
        return java_expression;
    }

    public void setJava_expression(java_Expression java_expression) {
        this.java_expression = java_expression;
    }
    public java_SingleVariableAccess getJava_singlevariableaccess() {
        return java_singlevariableaccess;
    }

    public void setJava_singlevariableaccess(java_SingleVariableAccess java_singlevariableaccess) {
        this.java_singlevariableaccess = java_singlevariableaccess;
    }

}