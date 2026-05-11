





import java.util.List;
import java.util.ArrayList;

public class smm_MeasureRelationship extends SmmRelationship {

    private String influence;



    public smm_MeasureRelationship(
        String influence    ) {
        super(
        );
        this.influence = influence;
    }


    public String getInfluence() {
        return influence;
    }

    public void setInfluence(String influence) {
        this.influence = influence;
    }


}