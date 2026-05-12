





import java.util.List;
import java.util.ArrayList;

public class model_SavingsAccount  {

    private float interestRate;
    private String type;



    public model_SavingsAccount(
        float interestRate,        String type    ) {
        this.interestRate = interestRate;
        this.type = type;
    }


    public float getInterestrate() {
        return interestRate;
    }

    public void setInterestrate(float interestRate) {
        this.interestRate = interestRate;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}