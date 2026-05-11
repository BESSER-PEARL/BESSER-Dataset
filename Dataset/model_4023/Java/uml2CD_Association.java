





import java.util.List;
import java.util.ArrayList;

public class uml2CD_Association extends NamedElement {

    private String isDerived;





    private uml2CD_Package uml2cd_package;


    public uml2CD_Association(
        String isDerived    ) {
        super(
        );
        this.isDerived = isDerived;
    }


    public String getIsderived() {
        return isDerived;
    }

    public void setIsderived(String isDerived) {
        this.isDerived = isDerived;
    }

    public uml2CD_Package getUml2cd_package() {
        return uml2cd_package;
    }

    public void setUml2cd_package(uml2CD_Package uml2cd_package) {
        this.uml2cd_package = uml2cd_package;
    }

}