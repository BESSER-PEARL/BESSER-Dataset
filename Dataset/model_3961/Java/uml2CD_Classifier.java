





import java.util.List;
import java.util.ArrayList;

public class uml2CD_Classifier extends Namespace, Typpee {

    private boolean isAbstract;





    private uml2CD_Generalization uml2cd_generalization;




    private uml2CD_Generalization uml2cd_generalization;




    private List<uml2CD_Generalization> uml2cd_generalizations;


    public uml2CD_Classifier(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.uml2cd_generalizations = new ArrayList<>();
    }

    public uml2CD_Classifier(
        boolean isAbstract        ArrayList<uml2CD_Generalization> uml2cd_generalizations    ) {
        this.isAbstract = isAbstract;
        this.uml2cd_generalizations = uml2cd_generalizations;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public uml2CD_Generalization getUml2cd_generalization() {
        return uml2cd_generalization;
    }

    public void setUml2cd_generalization(uml2CD_Generalization uml2cd_generalization) {
        this.uml2cd_generalization = uml2cd_generalization;
    }
    public uml2CD_Generalization getUml2cd_generalization() {
        return uml2cd_generalization;
    }

    public void setUml2cd_generalization(uml2CD_Generalization uml2cd_generalization) {
        this.uml2cd_generalization = uml2cd_generalization;
    }
    public List<uml2CD_Generalization> getUml2cd_generalizations() {
        return uml2cd_generalizations;
    }

    public void addUml2cd_generalization(Uml2cd_generalization uml2cd_generalization) {
        this.uml2cd_generalizations.add(uml2cd_generalization);
    }

}