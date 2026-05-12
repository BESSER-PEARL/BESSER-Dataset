





import java.util.List;
import java.util.ArrayList;

public class bank_Account  {

    private float credit;
    private float overdraft;



    public bank_Account(
        float credit,        float overdraft    ) {
        this.credit = credit;
        this.overdraft = overdraft;
    }


    public float getCredit() {
        return credit;
    }

    public void setCredit(float credit) {
        this.credit = credit;
    }
    public float getOverdraft() {
        return overdraft;
    }

    public void setOverdraft(float overdraft) {
        this.overdraft = overdraft;
    }


}