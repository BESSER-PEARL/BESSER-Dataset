





import java.util.List;
import java.util.ArrayList;

public class uma_ActivityDescription extends BreakdownElementDescription {

    private String purpose;
    private String alternatives;
    private String howToStaff;



    public uma_ActivityDescription(
        String purpose,        String alternatives,        String howToStaff    ) {
        super(
        );
        this.purpose = purpose;
        this.alternatives = alternatives;
        this.howToStaff = howToStaff;
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
    public String getHowtostaff() {
        return howToStaff;
    }

    public void setHowtostaff(String howToStaff) {
        this.howToStaff = howToStaff;
    }


}