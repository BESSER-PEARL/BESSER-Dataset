





import java.util.List;
import java.util.ArrayList;

public class safetyDSL_NonSafetyCritical extends ArchitecturalElement {






    private List<safetyDSL_NonSafetyCritical> safetydsl_nonsafetycriticals;


    public safetyDSL_NonSafetyCritical(
    ) {
        super(
        );
        this.safetydsl_nonsafetycriticals = new ArrayList<>();
    }

    public safetyDSL_NonSafetyCritical(
        ArrayList<safetyDSL_NonSafetyCritical> safetydsl_nonsafetycriticals    ) {
        this.safetydsl_nonsafetycriticals = safetydsl_nonsafetycriticals;
    }


    public List<safetyDSL_NonSafetyCritical> getSafetydsl_nonsafetycriticals() {
        return safetydsl_nonsafetycriticals;
    }

    public void addSafetydsl_nonsafetycritical(Safetydsl_nonsafetycritical safetydsl_nonsafetycritical) {
        this.safetydsl_nonsafetycriticals.add(safetydsl_nonsafetycritical);
    }

}