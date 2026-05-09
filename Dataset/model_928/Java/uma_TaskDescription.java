





import java.util.List;
import java.util.ArrayList;

public class uma_TaskDescription extends ContentDescription {

    private String purpose;
    private String alternatives;



    public uma_TaskDescription(
        String purpose,        String alternatives    ) {
        super(
        );
        this.purpose = purpose;
        this.alternatives = alternatives;
    }


    public String getPurpose() {
        return purpose;
    }

    public void setPurpose(String purpose) {
        this.purpose = purpose;
    }
    public String getAlternatives() {
        return alternatives;
    }

    public void setAlternatives(String alternatives) {
        this.alternatives = alternatives;
    }


}