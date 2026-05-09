





import java.util.List;
import java.util.ArrayList;

public class java_VariableDeclaration extends NamedElement {

    private int extraArrayDimensions;





    private java_SingleVariableAccess java_singlevariableaccess;




    private List<java_SingleVariableAccess> java_singlevariableaccesss;




    private java_Expression java_expression;


    public java_VariableDeclaration(
        int extraArrayDimensions    ) {
        super(
        );
        this.extraArrayDimensions = extraArrayDimensions;
        this.java_singlevariableaccesss = new ArrayList<>();
    }

    public java_VariableDeclaration(
        int extraArrayDimensions        ArrayList<java_SingleVariableAccess> java_singlevariableaccesss    ) {
        this.extraArrayDimensions = extraArrayDimensions;
        this.java_singlevariableaccesss = java_singlevariableaccesss;
    }

    public int getExtraarraydimensions() {
        return extraArrayDimensions;
    }

    public void setExtraarraydimensions(int extraArrayDimensions) {
        this.extraArrayDimensions = extraArrayDimensions;
    }

    public java_SingleVariableAccess getJava_singlevariableaccess() {
        return java_singlevariableaccess;
    }

    public void setJava_singlevariableaccess(java_SingleVariableAccess java_singlevariableaccess) {
        this.java_singlevariableaccess = java_singlevariableaccess;
    }
    public List<java_SingleVariableAccess> getJava_singlevariableaccesss() {
        return java_singlevariableaccesss;
    }

    public void addJava_singlevariableaccess(Java_singlevariableaccess java_singlevariableaccess) {
        this.java_singlevariableaccesss.add(java_singlevariableaccess);
    }
    public java_Expression getJava_expression() {
        return java_expression;
    }

    public void setJava_expression(java_Expression java_expression) {
        this.java_expression = java_expression;
    }

}