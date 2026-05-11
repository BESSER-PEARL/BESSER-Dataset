





import java.util.List;
import java.util.ArrayList;

public class smm_SmmModel extends SmmElement {






    private List<smm_SmmElement> smm_smmelements;




    private smm_SmmElement smm_smmelement;


    public smm_SmmModel(
    ) {
        super(
        );
        this.smm_smmelements = new ArrayList<>();
    }

    public smm_SmmModel(
        ArrayList<smm_SmmElement> smm_smmelements    ) {
        this.smm_smmelements = smm_smmelements;
    }


    public List<smm_SmmElement> getSmm_smmelements() {
        return smm_smmelements;
    }

    public void addSmm_smmelement(Smm_smmelement smm_smmelement) {
        this.smm_smmelements.add(smm_smmelement);
    }
    public smm_SmmElement getSmm_smmelement() {
        return smm_smmelement;
    }

    public void setSmm_smmelement(smm_SmmElement smm_smmelement) {
        this.smm_smmelement = smm_smmelement;
    }

}