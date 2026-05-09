





import java.util.List;
import java.util.ArrayList;

public class uma_Activity extends VariabilityElement, WorkDefinition, WorkBreakdownElement {

    private String isEnactable;





    private uma_BreakdownElement uma_breakdownelement;




    private List<uma_BreakdownElement> uma_breakdownelements;


    public uma_Activity(
        String isEnactable    ) {
        super(
        );
        this.isEnactable = isEnactable;
        this.uma_breakdownelements = new ArrayList<>();
    }

    public uma_Activity(
        String isEnactable        ArrayList<uma_BreakdownElement> uma_breakdownelements    ) {
        this.isEnactable = isEnactable;
        this.uma_breakdownelements = uma_breakdownelements;
    }

    public String getIsenactable() {
        return isEnactable;
    }

    public void setIsenactable(String isEnactable) {
        this.isEnactable = isEnactable;
    }

    public uma_BreakdownElement getUma_breakdownelement() {
        return uma_breakdownelement;
    }

    public void setUma_breakdownelement(uma_BreakdownElement uma_breakdownelement) {
        this.uma_breakdownelement = uma_breakdownelement;
    }
    public List<uma_BreakdownElement> getUma_breakdownelements() {
        return uma_breakdownelements;
    }

    public void addUma_breakdownelement(Uma_breakdownelement uma_breakdownelement) {
        this.uma_breakdownelements.add(uma_breakdownelement);
    }

}