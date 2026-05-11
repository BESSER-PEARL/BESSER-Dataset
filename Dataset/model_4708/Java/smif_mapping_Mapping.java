





import java.util.List;
import java.util.ArrayList;

public class smif_mapping_Mapping extends constraints_Rule, patterns_Pattern {

    private String strength;



    public smif_mapping_Mapping(
        String strength    ) {
        super(
        );
        this.strength = strength;
    }


    public String getStrength() {
        return strength;
    }

    public void setStrength(String strength) {
        this.strength = strength;
    }


}