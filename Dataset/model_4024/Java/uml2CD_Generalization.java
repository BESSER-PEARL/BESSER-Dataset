





import java.util.List;
import java.util.ArrayList;

public class uml2CD_Generalization  {

    private String isSubstitutable;





    private uml2CD_Class uml2cd_class;




    private uml2CD_Package uml2cd_package;




    private uml2CD_Class uml2cd_class;




    private List<uml2CD_GeneralizationSet> uml2cd_generalizationsets;


    public uml2CD_Generalization(
        String isSubstitutable    ) {
        this.isSubstitutable = isSubstitutable;
        this.uml2cd_generalizationsets = new ArrayList<>();
    }

    public uml2CD_Generalization(
        String isSubstitutable        ArrayList<uml2CD_GeneralizationSet> uml2cd_generalizationsets    ) {
        this.isSubstitutable = isSubstitutable;
        this.uml2cd_generalizationsets = uml2cd_generalizationsets;
    }

    public String getIssubstitutable() {
        return isSubstitutable;
    }

    public void setIssubstitutable(String isSubstitutable) {
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
    public List<uml2CD_GeneralizationSet> getUml2cd_generalizationsets() {
        return uml2cd_generalizationsets;
    }

    public void addUml2cd_generalizationset(Uml2cd_generalizationset uml2cd_generalizationset) {
        this.uml2cd_generalizationsets.add(uml2cd_generalizationset);
    }

}