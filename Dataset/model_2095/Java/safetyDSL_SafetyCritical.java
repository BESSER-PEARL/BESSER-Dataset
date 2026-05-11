





import java.util.List;
import java.util.ArrayList;

public class safetyDSL_SafetyCritical extends ArchitecturalElement {






    private List<safetyDSL_SafetyRequirement> safetydsl_safetyrequirements;




    private List<safetyDSL_SafetyCritical> safetydsl_safetycriticals;


    public safetyDSL_SafetyCritical(
    ) {
        super(
        );
        this.safetydsl_safetyrequirements = new ArrayList<>();
        this.safetydsl_safetycriticals = new ArrayList<>();
    }

    public safetyDSL_SafetyCritical(
        ArrayList<safetyDSL_SafetyRequirement> safetydsl_safetyrequirements,        ArrayList<safetyDSL_SafetyCritical> safetydsl_safetycriticals    ) {
        this.safetydsl_safetyrequirements = safetydsl_safetyrequirements;
        this.safetydsl_safetycriticals = safetydsl_safetycriticals;
    }


    public List<safetyDSL_SafetyRequirement> getSafetydsl_safetyrequirements() {
        return safetydsl_safetyrequirements;
    }

    public void addSafetydsl_safetyrequirement(Safetydsl_safetyrequirement safetydsl_safetyrequirement) {
        this.safetydsl_safetyrequirements.add(safetydsl_safetyrequirement);
    }
    public List<safetyDSL_SafetyCritical> getSafetydsl_safetycriticals() {
        return safetydsl_safetycriticals;
    }

    public void addSafetydsl_safetycritical(Safetydsl_safetycritical safetydsl_safetycritical) {
        this.safetydsl_safetycriticals.add(safetydsl_safetycritical);
    }

}