





import java.util.List;
import java.util.ArrayList;

public class CurrentAccount  {

    private String HolderName;
    private int AccNo;
    private int PIn;



    public CurrentAccount(
        String HolderName,        int AccNo,        int PIn    ) {
        this.HolderName = HolderName;
        this.AccNo = AccNo;
        this.PIn = PIn;
    }


    public String getHoldername() {
        return HolderName;
    }

    public void setHoldername(String HolderName) {
        this.HolderName = HolderName;
    }
    public int getAccno() {
        return AccNo;
    }

    public void setAccno(int AccNo) {
        this.AccNo = AccNo;
    }
    public int getPin() {
        return PIn;
    }

    public void setPin(int PIn) {
        this.PIn = PIn;
    }


}