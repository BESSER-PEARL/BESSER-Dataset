





import java.util.List;
import java.util.ArrayList;

public class CoDTransaction  {

    private String interestRate;
    private String endDate;
    private String startDate;



    public CoDTransaction(
        String interestRate,        String endDate,        String startDate    ) {
        this.interestRate = interestRate;
        this.endDate = endDate;
        this.startDate = startDate;
    }


    public String getInterestrate() {
        return interestRate;
    }

    public void setInterestrate(String interestRate) {
        this.interestRate = interestRate;
    }
    public String getEnddate() {
        return endDate;
    }

    public void setEnddate(String endDate) {
        this.endDate = endDate;
    }
    public String getStartdate() {
        return startDate;
    }

    public void setStartdate(String startDate) {
        this.startDate = startDate;
    }


}