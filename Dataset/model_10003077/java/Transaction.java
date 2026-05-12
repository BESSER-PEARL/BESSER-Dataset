





import java.util.List;
import java.util.ArrayList;

public class Transaction  {

    private String status;
    private int TranId;
    private String date;
    private None type;
    private int Acc_num;
    private int amount;
    private int prevBalance;
    private int currentBalance;





    private Account account;


    public Transaction(
        String status,        int TranId,        String date,        None type,        int Acc_num,        int amount,        int prevBalance,        int currentBalance    ) {
        this.status = status;
        this.TranId = TranId;
        this.date = date;
        this.type = type;
        this.Acc_num = Acc_num;
        this.amount = amount;
        this.prevBalance = prevBalance;
        this.currentBalance = currentBalance;
    }


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public int getTranid() {
        return TranId;
    }

    public void setTranid(int TranId) {
        this.TranId = TranId;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }
    public int getAcc_num() {
        return Acc_num;
    }

    public void setAcc_num(int Acc_num) {
        this.Acc_num = Acc_num;
    }
    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }
    public int getPrevbalance() {
        return prevBalance;
    }

    public void setPrevbalance(int prevBalance) {
        this.prevBalance = prevBalance;
    }
    public int getCurrentbalance() {
        return currentBalance;
    }

    public void setCurrentbalance(int currentBalance) {
        this.currentBalance = currentBalance;
    }

    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }

}