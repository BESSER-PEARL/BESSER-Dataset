





import java.util.List;
import java.util.ArrayList;

public class uma_ActivityDescription extends BreakdownElementDescription {

    private String howtoStaff;
    private String purpose;
    private String alternatives;



    public uma_ActivityDescription(
        String howtoStaff,        String purpose,        String alternatives    ) {
        super(
        );
        this.howtoStaff = howtoStaff;
        this.purpose = purpose;
        this.alternatives = alternatives;
    }


    public String getHowtostaff() {
        return howtoStaff;
    }

    public void setHowtostaff(String howtoStaff) {
        this.howtoStaff = howtoStaff;
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