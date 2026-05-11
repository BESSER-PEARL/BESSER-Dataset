





import java.util.List;
import java.util.ArrayList;

public class smm_MeasureRelationship extends SmmRelationship {

    private String influence;





    private smm_Operation smm_operation;


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

    public smm_Operation getSmm_operation() {
        return smm_operation;
    }

    public void setSmm_operation(smm_Operation smm_operation) {
        this.smm_operation = smm_operation;
    }

}