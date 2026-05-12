





import java.util.List;
import java.util.ArrayList;

public class Creator  {

    private String name;
    private boolean folded;
    private float currentBet;
    private float money;



    public Creator(
        String name,        boolean folded,        float currentBet,        float money    ) {
        this.name = name;
        this.folded = folded;
        this.currentBet = currentBet;
        this.money = money;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getFolded() {
        return folded;
    }

    public void setFolded(boolean folded) {
        this.folded = folded;
    }
    public float getCurrentbet() {
        return currentBet;
    }

    public void setCurrentbet(float currentBet) {
        this.currentBet = currentBet;
    }
    public float getMoney() {
        return money;
    }

    public void setMoney(float money) {
        this.money = money;
    }


}