





import java.util.List;
import java.util.ArrayList;

public class core_ReferencedModelElements extends IdentifiedElement {

    private String agregationType;





    private List<core_ModelElementReference> core_modelelementreferences;




    private core_ContractualElement core_contractualelement;




    private core_ModelElementReference core_modelelementreference;


    public core_ReferencedModelElements(
        String agregationType    ) {
        super(
        );
        this.agregationType = agregationType;
        this.core_modelelementreferences = new ArrayList<>();
    }

    public core_ReferencedModelElements(
        String agregationType        ArrayList<core_ModelElementReference> core_modelelementreferences    ) {
        this.agregationType = agregationType;
        this.core_modelelementreferences = core_modelelementreferences;
    }

    public String getAgregationtype() {
        return agregationType;
    }

    public void setAgregationtype(String agregationType) {
        this.agregationType = agregationType;
    }

    public List<core_ModelElementReference> getCore_modelelementreferences() {
        return core_modelelementreferences;
    }

    public void addCore_modelelementreference(Core_modelelementreference core_modelelementreference) {
        this.core_modelelementreferences.add(core_modelelementreference);
    }
    public core_ContractualElement getCore_contractualelement() {
        return core_contractualelement;
    }

    public void setCore_contractualelement(core_ContractualElement core_contractualelement) {
        this.core_contractualelement = core_contractualelement;
    }
    public core_ModelElementReference getCore_modelelementreference() {
        return core_modelelementreference;
    }

    public void setCore_modelelementreference(core_ModelElementReference core_modelelementreference) {
        this.core_modelelementreference = core_modelelementreference;
    }

}