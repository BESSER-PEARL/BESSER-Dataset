





import java.util.List;
import java.util.ArrayList;

public class Profile  {

    private String username;
    private int money;



    public Profile(
        String username,        int money    ) {
        this.username = username;
        this.money = money;
    }


    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public int getMoney() {
        return money;
    }

    public void setMoney(int money) {
        this.money = money;
    }


}