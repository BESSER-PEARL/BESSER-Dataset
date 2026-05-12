





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private int Transaction_id_;
    private int Acc_No_;
    private int Amount_paid_;



    public Payment(
        int Transaction_id_,        int Acc_No_,        int Amount_paid_    ) {
        this.Transaction_id_ = Transaction_id_;
        this.Acc_No_ = Acc_No_;
        this.Amount_paid_ = Amount_paid_;
    }


    public int getTransaction_id_() {
        return Transaction_id_;
    }

    public void setTransaction_id_(int Transaction_id_) {
        this.Transaction_id_ = Transaction_id_;
    }
    public int getAcc_no_() {
        return Acc_No_;
    }

    public void setAcc_no_(int Acc_No_) {
        this.Acc_No_ = Acc_No_;
    }
    public int getAmount_paid_() {
        return Amount_paid_;
    }

    public void setAmount_paid_(int Amount_paid_) {
        this.Amount_paid_ = Amount_paid_;
    }


}