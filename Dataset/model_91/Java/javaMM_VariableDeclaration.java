





import java.util.List;
import java.util.ArrayList;

public class javaMM_VariableDeclaration extends NamedElement {

    private int extraArrayDimensions;





    private javaMM_SingleVariableAccess javamm_singlevariableaccess;




    private List<javaMM_SingleVariableAccess> javamm_singlevariableaccesss;


    public javaMM_VariableDeclaration(
        int extraArrayDimensions    ) {
        super(
        );
        this.extraArrayDimensions = extraArrayDimensions;
        this.javamm_singlevariableaccesss = new ArrayList<>();
    }

    public javaMM_VariableDeclaration(
        int extraArrayDimensions        ArrayList<javaMM_SingleVariableAccess> javamm_singlevariableaccesss    ) {
        this.extraArrayDimensions = extraArrayDimensions;
        this.javamm_singlevariableaccesss = javamm_singlevariableaccesss;
    }

    public int getExtraarraydimensions() {
        return extraArrayDimensions;
    }

    public void setExtraarraydimensions(int extraArrayDimensions) {
        this.extraArrayDimensions = extraArrayDimensions;
    }

    public javaMM_SingleVariableAccess getJavamm_singlevariableaccess() {
        return javamm_singlevariableaccess;
    }

    public void setJavamm_singlevariableaccess(javaMM_SingleVariableAccess javamm_singlevariableaccess) {
        this.javamm_singlevariableaccess = javamm_singlevariableaccess;
    }
    public List<javaMM_SingleVariableAccess> getJavamm_singlevariableaccesss() {
        return javamm_singlevariableaccesss;
    }

    public void addJavamm_singlevariableaccess(Javamm_singlevariableaccess javamm_singlevariableaccess) {
        this.javamm_singlevariableaccesss.add(javamm_singlevariableaccess);
    }

}