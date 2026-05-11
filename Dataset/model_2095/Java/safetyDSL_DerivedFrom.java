





import java.util.List;
import java.util.ArrayList;

public class safetyDSL_DerivedFrom extends HazardRelation {






    private List<safetyDSL_SafetyRequirement> safetydsl_safetyrequirements;


    public safetyDSL_DerivedFrom(
    ) {
        super(
        );
        this.safetydsl_safetyrequirements = new ArrayList<>();
    }

    public safetyDSL_DerivedFrom(
        ArrayList<safetyDSL_SafetyRequirement> safetydsl_safetyrequirements    ) {
        this.safetydsl_safetyrequirements = safetydsl_safetyrequirements;
    }


    public List<safetyDSL_SafetyRequirement> getSafetydsl_safetyrequirements() {
        return safetydsl_safetyrequirements;
    }

    public void addSafetydsl_safetyrequirement(Safetydsl_safetyrequirement safetydsl_safetyrequirement) {
        this.safetydsl_safetyrequirements.add(safetydsl_safetyrequirement);
    }

}