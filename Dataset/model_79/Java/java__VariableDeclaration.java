





import java.util.List;
import java.util.ArrayList;

public class java__VariableDeclaration extends NamedElement {

    private int extraArrayDimensions;





    private java__Expression java__expression;




    private java__SingleVariableAccess java__singlevariableaccess;




    private List<java__SingleVariableAccess> java__singlevariableaccesss;


    public java__VariableDeclaration(
        int extraArrayDimensions    ) {
        super(
        );
        this.extraArrayDimensions = extraArrayDimensions;
        this.java__singlevariableaccesss = new ArrayList<>();
    }

    public java__VariableDeclaration(
        int extraArrayDimensions        ArrayList<java__SingleVariableAccess> java__singlevariableaccesss    ) {
        this.extraArrayDimensions = extraArrayDimensions;
        this.java__singlevariableaccesss = java__singlevariableaccesss;
    }

    public int getExtraarraydimensions() {
        return extraArrayDimensions;
    }

    public void setExtraarraydimensions(int extraArrayDimensions) {
        this.extraArrayDimensions = extraArrayDimensions;
    }

    public java__Expression getJava__expression() {
        return java__expression;
    }

    public void setJava__expression(java__Expression java__expression) {
        this.java__expression = java__expression;
    }
    public java__SingleVariableAccess getJava__singlevariableaccess() {
        return java__singlevariableaccess;
    }

    public void setJava__singlevariableaccess(java__SingleVariableAccess java__singlevariableaccess) {
        this.java__singlevariableaccess = java__singlevariableaccess;
    }
    public List<java__SingleVariableAccess> getJava__singlevariableaccesss() {
        return java__singlevariableaccesss;
    }

    public void addJava__singlevariableaccess(Java__singlevariableaccess java__singlevariableaccess) {
        this.java__singlevariableaccesss.add(java__singlevariableaccess);
    }

}