





import java.util.List;
import java.util.ArrayList;

public class core_ReferencedModelElements extends IdentifiedElement {

    private String agregationType;





    private core_ContractualElement core_contractualelement;


    public core_ReferencedModelElements(
        String agregationType    ) {
        super(
        );
        this.agregationType = agregationType;
    }


    public String getAgregationtype() {
        return agregationType;
    }

    public void setAgregationtype(String agregationType) {
        this.agregationType = agregationType;
    }

    public core_ContractualElement getCore_contractualelement() {
        return core_contractualelement;
    }

    public void setCore_contractualelement(core_ContractualElement core_contractualelement) {
        this.core_contractualelement = core_contractualelement;
    }

}