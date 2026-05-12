





import java.util.List;
import java.util.ArrayList;

public class Medical_Record_CertificatesOfDepositAccount  {

    private int timePeriod;
    private float interestRate;



    public Medical_Record_CertificatesOfDepositAccount(
        int timePeriod,        float interestRate    ) {
        this.timePeriod = timePeriod;
        this.interestRate = interestRate;
    }


    public int getTimeperiod() {
        return timePeriod;
    }

    public void setTimeperiod(int timePeriod) {
        this.timePeriod = timePeriod;
    }
    public float getInterestrate() {
        return interestRate;
    }

    public void setInterestrate(float interestRate) {
        this.interestRate = interestRate;
    }


}