





import java.util.List;
import java.util.ArrayList;

public class SavingsAccount  {

    private float interestRate;
    private boolean noticeGiven;



    public SavingsAccount(
        float interestRate,        boolean noticeGiven    ) {
        this.interestRate = interestRate;
        this.noticeGiven = noticeGiven;
    }


    public float getInterestrate() {
        return interestRate;
    }

    public void setInterestrate(float interestRate) {
        this.interestRate = interestRate;
    }
    public boolean getNoticegiven() {
        return noticeGiven;
    }

    public void setNoticegiven(boolean noticeGiven) {
        this.noticeGiven = noticeGiven;
    }


}