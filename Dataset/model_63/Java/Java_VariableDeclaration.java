





import java.util.List;
import java.util.ArrayList;

public class Java_VariableDeclaration extends NamedElement {

    private int extraArrayDimensions;





    private Java_Expression java_expression;




    private List<Java_SingleVariableAccess> java_singlevariableaccesss;




    private Java_SingleVariableAccess java_singlevariableaccess;


    public Java_VariableDeclaration(
        int extraArrayDimensions    ) {
        super(
        );
        this.extraArrayDimensions = extraArrayDimensions;
        this.java_singlevariableaccesss = new ArrayList<>();
    }

    public Java_VariableDeclaration(
        int extraArrayDimensions        ArrayList<Java_SingleVariableAccess> java_singlevariableaccesss    ) {
        this.extraArrayDimensions = extraArrayDimensions;
        this.java_singlevariableaccesss = java_singlevariableaccesss;
    }

    public int getExtraarraydimensions() {
        return extraArrayDimensions;
    }

    public void setExtraarraydimensions(int extraArrayDimensions) {
        this.extraArrayDimensions = extraArrayDimensions;
    }

    public Java_Expression getJava_expression() {
        return java_expression;
    }

    public void setJava_expression(Java_Expression java_expression) {
        this.java_expression = java_expression;
    }
    public List<Java_SingleVariableAccess> getJava_singlevariableaccesss() {
        return java_singlevariableaccesss;
    }

    public void addJava_singlevariableaccess(Java_singlevariableaccess java_singlevariableaccess) {
        this.java_singlevariableaccesss.add(java_singlevariableaccess);
    }
    public Java_SingleVariableAccess getJava_singlevariableaccess() {
        return java_singlevariableaccess;
    }

    public void setJava_singlevariableaccess(Java_SingleVariableAccess java_singlevariableaccess) {
        this.java_singlevariableaccess = java_singlevariableaccess;
    }

}