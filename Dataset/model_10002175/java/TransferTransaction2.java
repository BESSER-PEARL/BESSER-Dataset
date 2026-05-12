





import java.util.List;
import java.util.ArrayList;

public class TransferTransaction2  {

    private String targetAccount;
    private String sourceAccount;



    public TransferTransaction2(
        String targetAccount,        String sourceAccount    ) {
        this.targetAccount = targetAccount;
        this.sourceAccount = sourceAccount;
    }


    public String getTargetaccount() {
        return targetAccount;
    }

    public void setTargetaccount(String targetAccount) {
        this.targetAccount = targetAccount;
    }
    public String getSourceaccount() {
        return sourceAccount;
    }

    public void setSourceaccount(String sourceAccount) {
        this.sourceAccount = sourceAccount;
    }


}