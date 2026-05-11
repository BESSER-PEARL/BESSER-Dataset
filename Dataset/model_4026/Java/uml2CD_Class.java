





import java.util.List;
import java.util.ArrayList;

public class uml2CD_Class extends NamedElement {

    private String active;





    private uml2CD_Generalization uml2cd_generalization;




    private uml2CD_Package uml2cd_package;




    private uml2CD_Generalization uml2cd_generalization;


    public uml2CD_Class(
        String active    ) {
        super(
        );
        this.active = active;
    }


    public String getActive() {
        return active;
    }

    public void setActive(String active) {
        this.active = active;
    }

    public uml2CD_Generalization getUml2cd_generalization() {
        return uml2cd_generalization;
    }

    public void setUml2cd_generalization(uml2CD_Generalization uml2cd_generalization) {
        this.uml2cd_generalization = uml2cd_generalization;
    }
    public uml2CD_Package getUml2cd_package() {
        return uml2cd_package;
    }

    public void setUml2cd_package(uml2CD_Package uml2cd_package) {
        this.uml2cd_package = uml2cd_package;
    }
    public uml2CD_Generalization getUml2cd_generalization() {
        return uml2cd_generalization;
    }

    public void setUml2cd_generalization(uml2CD_Generalization uml2cd_generalization) {
        this.uml2cd_generalization = uml2cd_generalization;
    }

}