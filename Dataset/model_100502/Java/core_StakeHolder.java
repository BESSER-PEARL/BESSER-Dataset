





import java.util.List;
import java.util.ArrayList;

public class core_StakeHolder extends Actor {






    private List<core_Rationale> core_rationales;




    private List<core_ContractualElement> core_contractualelements;




    private core_ContractualElement core_contractualelement;


    public core_StakeHolder(
    ) {
        super(
        );
        this.core_rationales = new ArrayList<>();
        this.core_contractualelements = new ArrayList<>();
    }

    public core_StakeHolder(
        ArrayList<core_Rationale> core_rationales,        ArrayList<core_ContractualElement> core_contractualelements    ) {
        this.core_rationales = core_rationales;
        this.core_contractualelements = core_contractualelements;
    }


    public List<core_Rationale> getCore_rationales() {
        return core_rationales;
    }

    public void addCore_rationale(Core_rationale core_rationale) {
        this.core_rationales.add(core_rationale);
    }
    public List<core_ContractualElement> getCore_contractualelements() {
        return core_contractualelements;
    }

    public void addCore_contractualelement(Core_contractualelement core_contractualelement) {
        this.core_contractualelements.add(core_contractualelement);
    }
    public core_ContractualElement getCore_contractualelement() {
        return core_contractualelement;
    }

    public void setCore_contractualelement(core_ContractualElement core_contractualelement) {
        this.core_contractualelement = core_contractualelement;
    }

}