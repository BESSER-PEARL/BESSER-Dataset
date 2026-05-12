





import java.util.List;
import java.util.ArrayList;

public class Savings_Account  {

    private int AccNo;
    private String Holder_Name;
    private None PIn;



    public Savings_Account(
        int AccNo,        String Holder_Name,        None PIn    ) {
        this.AccNo = AccNo;
        this.Holder_Name = Holder_Name;
        this.PIn = PIn;
    }


    public int getAccno() {
        return AccNo;
    }

    public void setAccno(int AccNo) {
        this.AccNo = AccNo;
    }
    public String getHolder_name() {
        return Holder_Name;
    }

    public void setHolder_name(String Holder_Name) {
        this.Holder_Name = Holder_Name;
    }
    public None getPin() {
        return PIn;
    }

    public void setPin(None PIn) {
        this.PIn = PIn;
    }


}