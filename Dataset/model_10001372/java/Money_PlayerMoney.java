





import java.util.List;
import java.util.ArrayList;

public class Money_PlayerMoney  {

    private String numofplayers;
    private String totalmoney;



    public Money_PlayerMoney(
        String numofplayers,        String totalmoney    ) {
        this.numofplayers = numofplayers;
        this.totalmoney = totalmoney;
    }


    public String getNumofplayers() {
        return numofplayers;
    }

    public void setNumofplayers(String numofplayers) {
        this.numofplayers = numofplayers;
    }
    public String getTotalmoney() {
        return totalmoney;
    }

    public void setTotalmoney(String totalmoney) {
        this.totalmoney = totalmoney;
    }


}