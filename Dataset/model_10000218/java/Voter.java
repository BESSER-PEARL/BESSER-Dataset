





import java.util.List;
import java.util.ArrayList;

public class Voter  {

    private int serialNum;
    private String password;



    public Voter(
        int serialNum,        String password    ) {
        this.serialNum = serialNum;
        this.password = password;
    }


    public int getSerialnum() {
        return serialNum;
    }

    public void setSerialnum(int serialNum) {
        this.serialNum = serialNum;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}