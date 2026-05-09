





import java.util.List;
import java.util.ArrayList;

public class java_VariableDeclaration extends NamedElement {

    private int extraArrayDimensions;





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

    public java_SingleVariableAccess getJava_singlevariableaccess() {
        return java_singlevariableaccess;
    }

    public void setJava_singlevariableaccess(java_SingleVariableAccess java_singlevariableaccess) {
        this.java_singlevariableaccess = java_singlevariableaccess;
    }

}