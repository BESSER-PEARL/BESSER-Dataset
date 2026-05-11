





import java.util.List;
import java.util.ArrayList;

public class safetyDSL_MonitorToArchitecturalElement extends SafetyCriticalRelation {






    private safetyDSL_Monitor safetydsl_monitor;




    private List<safetyDSL_SafetyCritical> safetydsl_safetycriticals;


    public safetyDSL_MonitorToArchitecturalElement(
    ) {
        super(
        );
        this.safetydsl_safetycriticals = new ArrayList<>();
    }

    public safetyDSL_MonitorToArchitecturalElement(
        ArrayList<safetyDSL_SafetyCritical> safetydsl_safetycriticals    ) {
        this.safetydsl_safetycriticals = safetydsl_safetycriticals;
    }


    public safetyDSL_Monitor getSafetydsl_monitor() {
        return safetydsl_monitor;
    }

    public void setSafetydsl_monitor(safetyDSL_Monitor safetydsl_monitor) {
        this.safetydsl_monitor = safetydsl_monitor;
    }
    public List<safetyDSL_SafetyCritical> getSafetydsl_safetycriticals() {
        return safetydsl_safetycriticals;
    }

    public void addSafetydsl_safetycritical(Safetydsl_safetycritical safetydsl_safetycritical) {
        this.safetydsl_safetycriticals.add(safetydsl_safetycritical);
    }

}