





import java.util.List;
import java.util.ArrayList;

public class BankingSystem_Saving extends Account {

    private float interestRate;



    public BankingSystem_Saving(
        float interestRate    ) {
        super(
        );
        this.interestRate = interestRate;
    }


    public float getInterestrate() {
        return interestRate;
    }

    public void setInterestrate(float interestRate) {
        this.interestRate = interestRate;
    }


}