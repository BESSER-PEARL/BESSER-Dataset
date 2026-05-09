





import java.util.List;
import java.util.ArrayList;

public class spem_Activity extends WorkBreakdownElement, WorkDefinition, VariabilityElement {

    private boolean isEnactable;
    private String useKind;





    private List<spem_ProcessParameter> spem_processparameters;




    private spem_ProcessPerformer spem_processperformer;




    private List<spem_BreakdownElement> spem_breakdownelements;




    private spem_Activity spem_activity;




    private List<spem_BreakdownElement> spem_breakdownelements;


    public spem_Activity(
        boolean isEnactable,        String useKind    ) {
        super(
        );
        this.isEnactable = isEnactable;
        this.useKind = useKind;
        this.spem_processparameters = new ArrayList<>();
        this.spem_breakdownelements = new ArrayList<>();
        this.spem_breakdownelements = new ArrayList<>();
    }

    public spem_Activity(
        boolean isEnactable,        String useKind        ArrayList<spem_ProcessParameter> spem_processparameters,        ArrayList<spem_BreakdownElement> spem_breakdownelements,        ArrayList<spem_BreakdownElement> spem_breakdownelements    ) {
        this.isEnactable = isEnactable;
        this.useKind = useKind;
        this.spem_processparameters = spem_processparameters;
        this.spem_breakdownelements = spem_breakdownelements;
        this.spem_breakdownelements = spem_breakdownelements;
    }

    public boolean getIsenactable() {
        return isEnactable;
    }

    public void setIsenactable(boolean isEnactable) {
        this.isEnactable = isEnactable;
    }
    public String getUsekind() {
        return useKind;
    }

    public void setUsekind(String useKind) {
        this.useKind = useKind;
    }

    public List<spem_ProcessParameter> getSpem_processparameters() {
        return spem_processparameters;
    }

    public void addSpem_processparameter(Spem_processparameter spem_processparameter) {
        this.spem_processparameters.add(spem_processparameter);
    }
    public spem_ProcessPerformer getSpem_processperformer() {
        return spem_processperformer;
    }

    public void setSpem_processperformer(spem_ProcessPerformer spem_processperformer) {
        this.spem_processperformer = spem_processperformer;
    }
    public List<spem_BreakdownElement> getSpem_breakdownelements() {
        return spem_breakdownelements;
    }

    public void addSpem_breakdownelement(Spem_breakdownelement spem_breakdownelement) {
        this.spem_breakdownelements.add(spem_breakdownelement);
    }
    public spem_Activity getSpem_activity() {
        return spem_activity;
    }

    public void setSpem_activity(spem_Activity spem_activity) {
        this.spem_activity = spem_activity;
    }
    public List<spem_BreakdownElement> getSpem_breakdownelements() {
        return spem_breakdownelements;
    }

    public void addSpem_breakdownelement(Spem_breakdownelement spem_breakdownelement) {
        this.spem_breakdownelements.add(spem_breakdownelement);
    }

}