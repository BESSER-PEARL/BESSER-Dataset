





import java.util.List;
import java.util.ArrayList;

public class safetyDSL_SafetyTactic  {

    private String name;
    private String type;





    private List<safetyDSL_Fault> safetydsl_faults;




    private safetyDSL_SafetyTacticViewpoint safetydsl_safetytacticviewpoint;




    private safetyDSL_SafetyCritical safetydsl_safetycritical;




    private safetyDSL_Monitor safetydsl_monitor;


    public safetyDSL_SafetyTactic(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
        this.safetydsl_faults = new ArrayList<>();
    }

    public safetyDSL_SafetyTactic(
        String name,        String type        ArrayList<safetyDSL_Fault> safetydsl_faults    ) {
        this.name = name;
        this.type = type;
        this.safetydsl_faults = safetydsl_faults;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<safetyDSL_Fault> getSafetydsl_faults() {
        return safetydsl_faults;
    }

    public void addSafetydsl_fault(Safetydsl_fault safetydsl_fault) {
        this.safetydsl_faults.add(safetydsl_fault);
    }
    public safetyDSL_SafetyTacticViewpoint getSafetydsl_safetytacticviewpoint() {
        return safetydsl_safetytacticviewpoint;
    }

    public void setSafetydsl_safetytacticviewpoint(safetyDSL_SafetyTacticViewpoint safetydsl_safetytacticviewpoint) {
        this.safetydsl_safetytacticviewpoint = safetydsl_safetytacticviewpoint;
    }
    public safetyDSL_SafetyCritical getSafetydsl_safetycritical() {
        return safetydsl_safetycritical;
    }

    public void setSafetydsl_safetycritical(safetyDSL_SafetyCritical safetydsl_safetycritical) {
        this.safetydsl_safetycritical = safetydsl_safetycritical;
    }
    public safetyDSL_Monitor getSafetydsl_monitor() {
        return safetydsl_monitor;
    }

    public void setSafetydsl_monitor(safetyDSL_Monitor safetydsl_monitor) {
        this.safetydsl_monitor = safetydsl_monitor;
    }

}