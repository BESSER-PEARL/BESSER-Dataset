





import java.util.List;
import java.util.ArrayList;

public class TransferTransaction  {

    private String sourceAccount;
    private String targetAccount;



    public TransferTransaction(
        String sourceAccount,        String targetAccount    ) {
        this.sourceAccount = sourceAccount;
        this.targetAccount = targetAccount;
    }


    public String getSourceaccount() {
        return sourceAccount;
    }

    public void setSourceaccount(String sourceAccount) {
        this.sourceAccount = sourceAccount;
    }
    public String getTargetaccount() {
        return targetAccount;
    }

    public void setTargetaccount(String targetAccount) {
        this.targetAccount = targetAccount;
    }


}