





import java.util.List;
import java.util.ArrayList;

public class safetyDSL_ReportsFault extends SafetyCriticalRelation {






    private List<safetyDSL_SafetyCritical> safetydsl_safetycriticals;




    private safetyDSL_SafetyCritical safetydsl_safetycritical;


    public safetyDSL_ReportsFault(
    ) {
        super(
        );
        this.safetydsl_safetycriticals = new ArrayList<>();
    }

    public safetyDSL_ReportsFault(
        ArrayList<safetyDSL_SafetyCritical> safetydsl_safetycriticals    ) {
        this.safetydsl_safetycriticals = safetydsl_safetycriticals;
    }


    public List<safetyDSL_SafetyCritical> getSafetydsl_safetycriticals() {
        return safetydsl_safetycriticals;
    }

    public void addSafetydsl_safetycritical(Safetydsl_safetycritical safetydsl_safetycritical) {
        this.safetydsl_safetycriticals.add(safetydsl_safetycritical);
    }
    public safetyDSL_SafetyCritical getSafetydsl_safetycritical() {
        return safetydsl_safetycritical;
    }

    public void setSafetydsl_safetycritical(safetyDSL_SafetyCritical safetydsl_safetycritical) {
        this.safetydsl_safetycritical = safetydsl_safetycritical;
    }

}