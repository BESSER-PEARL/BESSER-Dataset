





import java.util.List;
import java.util.ArrayList;

public class Account  {

    private String Branch_;
    private int Phone_no_;
    private int Acc_no_;



    public Account(
        String Branch_,        int Phone_no_,        int Acc_no_    ) {
        this.Branch_ = Branch_;
        this.Phone_no_ = Phone_no_;
        this.Acc_no_ = Acc_no_;
    }


    public String getBranch_() {
        return Branch_;
    }

    public void setBranch_(String Branch_) {
        this.Branch_ = Branch_;
    }
    public int getPhone_no_() {
        return Phone_no_;
    }

    public void setPhone_no_(int Phone_no_) {
        this.Phone_no_ = Phone_no_;
    }
    public int getAcc_no_() {
        return Acc_no_;
    }

    public void setAcc_no_(int Acc_no_) {
        this.Acc_no_ = Acc_no_;
    }


}