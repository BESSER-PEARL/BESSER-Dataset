





import java.util.List;
import java.util.ArrayList;

public class TransferTransaction  {

    private None targetAccount;
    private None sourceAccount;



    public TransferTransaction(
        None targetAccount,        None sourceAccount    ) {
        this.targetAccount = targetAccount;
        this.sourceAccount = sourceAccount;
    }


    public None getTargetaccount() {
        return targetAccount;
    }

    public void setTargetaccount(None targetAccount) {
        this.targetAccount = targetAccount;
    }
    public None getSourceaccount() {
        return sourceAccount;
    }

    public void setSourceaccount(None sourceAccount) {
        this.sourceAccount = sourceAccount;
    }


}