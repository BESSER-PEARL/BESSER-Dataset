





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private int position;
    private String token;
    private int balance;
    private String name;



    public Player(
        int position,        String token,        int balance,        String name    ) {
        this.position = position;
        this.token = token;
        this.balance = balance;
        this.name = name;
    }


    public int getPosition() {
        return position;
    }

    public void setPosition(int position) {
        this.position = position;
    }
    public String getToken() {
        return token;
    }

    public void setToken(String token) {
        this.token = token;
    }
    public int getBalance() {
        return balance;
    }

    public void setBalance(int balance) {
        this.balance = balance;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}