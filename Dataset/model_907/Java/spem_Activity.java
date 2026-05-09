





import java.util.List;
import java.util.ArrayList;

public class spem_Activity extends WorkBreakdownElement, WorkDefinition, VariabilityElement {

    private boolean isEnactable;
    private String howToStaff;
    private String useKind;





    private spem_Activity spem_activity;




    private spem_Activity spem_activity;




    private List<spem_BreakdownElement> spem_breakdownelements;




    private List<spem_BreakdownElement> spem_breakdownelements;


    public spem_Activity(
        boolean isEnactable,        String howToStaff,        String useKind    ) {
        super(
        );
        this.isEnactable = isEnactable;
        this.howToStaff = howToStaff;
        this.useKind = useKind;
        this.spem_breakdownelements = new ArrayList<>();
        this.spem_breakdownelements = new ArrayList<>();
    }

    public spem_Activity(
        boolean isEnactable,        String howToStaff,        String useKind        ArrayList<spem_BreakdownElement> spem_breakdownelements,        ArrayList<spem_BreakdownElement> spem_breakdownelements    ) {
        this.isEnactable = isEnactable;
        this.howToStaff = howToStaff;
        this.useKind = useKind;
        this.spem_breakdownelements = spem_breakdownelements;
        this.spem_breakdownelements = spem_breakdownelements;
    }

    public boolean getIsenactable() {
        return isEnactable;
    }

    public void setIsenactable(boolean isEnactable) {
        this.isEnactable = isEnactable;
    }
    public String getHowtostaff() {
        return howToStaff;
    }

    public void setHowtostaff(String howToStaff) {
        this.howToStaff = howToStaff;
    }
    public String getUsekind() {
        return useKind;
    }

    public void setUsekind(String useKind) {
        this.useKind = useKind;
    }

    public spem_Activity getSpem_activity() {
        return spem_activity;
    }

    public void setSpem_activity(spem_Activity spem_activity) {
        this.spem_activity = spem_activity;
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
    public List<spem_BreakdownElement> getSpem_breakdownelements() {
        return spem_breakdownelements;
    }

    public void addSpem_breakdownelement(Spem_breakdownelement spem_breakdownelement) {
        this.spem_breakdownelements.add(spem_breakdownelement);
    }

}