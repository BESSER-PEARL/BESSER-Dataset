





import java.util.List;
import java.util.ArrayList;

public class uma_ActivityDescription extends BreakdownElementDescription {

    private String howtoStaff;
    private String alternatives;
    private String purpose;



    public uma_ActivityDescription(
        String howtoStaff,        String alternatives,        String purpose    ) {
        super(
        );
        this.howtoStaff = howtoStaff;
        this.alternatives = alternatives;
        this.purpose = purpose;
    }


    public String getHowtostaff() {
        return howtoStaff;
    }

    public void setHowtostaff(String howtoStaff) {
        this.howtoStaff = howtoStaff;
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