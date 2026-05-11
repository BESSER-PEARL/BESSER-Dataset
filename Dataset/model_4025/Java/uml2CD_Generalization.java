





import java.util.List;
import java.util.ArrayList;

public class uml2CD_Generalization  {

    private boolean isSubstitutable;





    private uml2CD_Class uml2cd_class;




    private uml2CD_Package uml2cd_package;




    private uml2CD_Class uml2cd_class;


    public uml2CD_Generalization(
        boolean isSubstitutable    ) {
        this.isSubstitutable = isSubstitutable;
    }


    public boolean getIssubstitutable() {
        return isSubstitutable;
    }

    public void setIssubstitutable(boolean isSubstitutable) {
        this.isSubstitutable = isSubstitutable;
    }

    public uml2CD_Class getUml2cd_class() {
        return uml2cd_class;
    }

    public void setUml2cd_class(uml2CD_Class uml2cd_class) {
        this.uml2cd_class = uml2cd_class;
    }
    public uml2CD_Package getUml2cd_package() {
        return uml2cd_package;
    }

    public void setUml2cd_package(uml2CD_Package uml2cd_package) {
        this.uml2cd_package = uml2cd_package;
    }
    public uml2CD_Class getUml2cd_class() {
        return uml2cd_class;
    }

    public void setUml2cd_class(uml2CD_Class uml2cd_class) {
        this.uml2cd_class = uml2cd_class;
    }

}