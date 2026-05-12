





import java.util.List;
import java.util.ArrayList;

public class statemachine_Transition extends Declaration {

    private String actionLabel;
    private String sourceLabel;
    private String label;
    private String targetLabel;
    private String guardLabel;



    public statemachine_Transition(
        String actionLabel,        String sourceLabel,        String label,        String targetLabel,        String guardLabel    ) {
        super(
        );
        this.actionLabel = actionLabel;
        this.sourceLabel = sourceLabel;
        this.label = label;
        this.targetLabel = targetLabel;
        this.guardLabel = guardLabel;
    }


    public String getActionlabel() {
        return actionLabel;
    }

    public void setActionlabel(String actionLabel) {
        this.actionLabel = actionLabel;
    }
    public String getSourcelabel() {
        return sourceLabel;
    }

    public void setSourcelabel(String sourceLabel) {
        this.sourceLabel = sourceLabel;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getTargetlabel() {
        return targetLabel;
    }

    public void setTargetlabel(String targetLabel) {
        this.targetLabel = targetLabel;
    }
    public String getGuardlabel() {
        return guardLabel;
    }

    public void setGuardlabel(String guardLabel) {
        this.guardLabel = guardLabel;
    }


}