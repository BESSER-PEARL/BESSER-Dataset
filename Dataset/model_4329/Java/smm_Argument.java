





import java.util.List;
import java.util.ArrayList;

public class smm_Argument extends SmmElement {

    private String value;
    private String Type;





    private smm_Observation smm_observation;


    public smm_Argument(
        String value,        String Type    ) {
        super(
        );
        this.value = value;
        this.Type = Type;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }

    public smm_Observation getSmm_observation() {
        return smm_observation;
    }

    public void setSmm_observation(smm_Observation smm_observation) {
        this.smm_observation = smm_observation;
    }

}