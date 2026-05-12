





import java.util.List;
import java.util.ArrayList;

public class Game_Display  {

    private String card;
    private String money;



    public Game_Display(
        String card,        String money    ) {
        this.card = card;
        this.money = money;
    }


    public String getCard() {
        return card;
    }

    public void setCard(String card) {
        this.card = card;
    }
    public String getMoney() {
        return money;
    }

    public void setMoney(String money) {
        this.money = money;
    }


}