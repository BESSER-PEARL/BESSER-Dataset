





import java.util.List;
import java.util.ArrayList;

public class CertificatesOfDepositAccount  {

    private float interestRate;
    private int timePeriod;



    public CertificatesOfDepositAccount(
        float interestRate,        int timePeriod    ) {
        this.interestRate = interestRate;
        this.timePeriod = timePeriod;
    }


    public float getInterestrate() {
        return interestRate;
    }

    public void setInterestrate(float interestRate) {
        this.interestRate = interestRate;
    }
    public int getTimeperiod() {
        return timePeriod;
    }

    public void setTimeperiod(int timePeriod) {
        this.timePeriod = timePeriod;
    }


}