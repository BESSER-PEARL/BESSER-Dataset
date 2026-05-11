





import java.util.List;
import java.util.ArrayList;

public class model_InfluenceRelationship extends DependendencyRelationship {

    private String strength;



    public model_InfluenceRelationship(
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