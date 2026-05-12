





import java.util.List;
import java.util.ArrayList;

public class TransferTransaction  {

    private None sourceAccount;
    private None targetAccount;



    public TransferTransaction(
        None sourceAccount,        None targetAccount    ) {
        this.sourceAccount = sourceAccount;
        this.targetAccount = targetAccount;
    }


    public None getSourceaccount() {
        return sourceAccount;
    }

    public void setSourceaccount(None sourceAccount) {
        this.sourceAccount = sourceAccount;
    }
    public None getTargetaccount() {
        return targetAccount;
    }

    public void setTargetaccount(None targetAccount) {
        this.targetAccount = targetAccount;
    }


}