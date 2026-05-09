





import java.util.List;
import java.util.ArrayList;

public class uma_TaskDescription extends ContentDescription {

    private String alternatives;
    private String purpose;



    public uma_TaskDescription(
        String alternatives,        String purpose    ) {
        super(
        );
        this.alternatives = alternatives;
        this.purpose = purpose;
    }


    public String getAlternatives() {
        return alternatives;
    }

    public void setAlternatives(String alternatives) {
        this.alternatives = alternatives;
    }
    public String getPurpose() {
        return purpose;
    }

    public void setPurpose(String purpose) {
        this.purpose = purpose;
    }


}