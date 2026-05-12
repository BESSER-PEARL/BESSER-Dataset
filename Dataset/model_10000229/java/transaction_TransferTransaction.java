





import java.util.List;
import java.util.ArrayList;

public class transaction_TransferTransaction  {

    private None sourceAccount;
    private None targetAccount;



    public transaction_TransferTransaction(
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