





import java.util.List;
import java.util.ArrayList;

public class uma_ActivityDescription extends BreakdownElementDescription {

    private String howToStaff;
    private String alternatives;
    private String purpose;



    public uma_ActivityDescription(
        String howToStaff,        String alternatives,        String purpose    ) {
        super(
        );
        this.howToStaff = howToStaff;
        this.alternatives = alternatives;
        this.purpose = purpose;
    }


    public String getHowtostaff() {
        return howToStaff;
    }

    public void setHowtostaff(String howToStaff) {
        this.howToStaff = howToStaff;
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