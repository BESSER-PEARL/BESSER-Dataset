





import java.util.List;
import java.util.ArrayList;

public class safetyDSL_Causes extends HazardRelation {






    private List<safetyDSL_Consequence> safetydsl_consequences;


    public safetyDSL_Causes(
    ) {
        super(
        );
        this.safetydsl_consequences = new ArrayList<>();
    }

    public safetyDSL_Causes(
        ArrayList<safetyDSL_Consequence> safetydsl_consequences    ) {
        this.safetydsl_consequences = safetydsl_consequences;
    }


    public List<safetyDSL_Consequence> getSafetydsl_consequences() {
        return safetydsl_consequences;
    }

    public void addSafetydsl_consequence(Safetydsl_consequence safetydsl_consequence) {
        this.safetydsl_consequences.add(safetydsl_consequence);
    }

}