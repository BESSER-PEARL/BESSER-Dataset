





import java.util.List;
import java.util.ArrayList;

public class uml2CD_BehavioralFeature extends Namespace, Feature {






    private List<uml2CD_Typpee> uml2cd_typpees;


    public uml2CD_BehavioralFeature(
    ) {
        super(
        );
        this.uml2cd_typpees = new ArrayList<>();
    }

    public uml2CD_BehavioralFeature(
        ArrayList<uml2CD_Typpee> uml2cd_typpees    ) {
        this.uml2cd_typpees = uml2cd_typpees;
    }


    public List<uml2CD_Typpee> getUml2cd_typpees() {
        return uml2cd_typpees;
    }

    public void addUml2cd_typpee(Uml2cd_typpee uml2cd_typpee) {
        this.uml2cd_typpees.add(uml2cd_typpee);
    }

}