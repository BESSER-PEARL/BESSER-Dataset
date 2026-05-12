





import java.util.List;
import java.util.ArrayList;

public class Regular_Members  {

    private int TriedPremium;
    private String TrialStartDate;



    public Regular_Members(
        int TriedPremium,        String TrialStartDate    ) {
        this.TriedPremium = TriedPremium;
        this.TrialStartDate = TrialStartDate;
    }


    public int getTriedpremium() {
        return TriedPremium;
    }

    public void setTriedpremium(int TriedPremium) {
        this.TriedPremium = TriedPremium;
    }
    public String getTrialstartdate() {
        return TrialStartDate;
    }

    public void setTrialstartdate(String TrialStartDate) {
        this.TrialStartDate = TrialStartDate;
    }


}