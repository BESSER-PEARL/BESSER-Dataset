





import java.util.List;
import java.util.ArrayList;

public class uma_ActivityDescription extends BreakdownElementDescription {

    private String purpose;
    private String howToStaff;
    private String alternatives;



    public uma_ActivityDescription(
        String purpose,        String howToStaff,        String alternatives    ) {
        super(
        );
        this.purpose = purpose;
        this.howToStaff = howToStaff;
        this.alternatives = alternatives;
    }


    public String getPurpose() {
        return purpose;
    }

    public void setPurpose(String purpose) {
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


}