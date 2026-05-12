





import java.util.List;
import java.util.ArrayList;

public class SavingsAccount  {

    private boolean noticeGiven;
    private float interestRate;



    public SavingsAccount(
        boolean noticeGiven,        float interestRate    ) {
        this.noticeGiven = noticeGiven;
        this.interestRate = interestRate;
    }


    public boolean getNoticegiven() {
        return noticeGiven;
    }

    public void setNoticegiven(boolean noticeGiven) {
        this.noticeGiven = noticeGiven;
    }
    public float getInterestrate() {
        return interestRate;
    }

    public void setInterestrate(float interestRate) {
        this.interestRate = interestRate;
    }


}