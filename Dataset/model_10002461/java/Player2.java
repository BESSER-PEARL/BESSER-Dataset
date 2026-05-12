





import java.util.List;
import java.util.ArrayList;

public class Player2  {

    private String name;





    private List<Game2> game2s;




    private List<Card2> card2s;




    private Avatar2 avatar2;


    public Player2(
        String name    ) {
        this.name = name;
        this.game2s = new ArrayList<>();
        this.card2s = new ArrayList<>();
    }

    public Player2(
        String name        ArrayList<Game2> game2s,        ArrayList<Card2> card2s    ) {
        this.name = name;
        this.game2s = game2s;
        this.card2s = card2s;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Game2> getGame2s() {
        return game2s;
    }

    public void addGame2(Game2 game2) {
        this.game2s.add(game2);
    }
    public List<Card2> getCard2s() {
        return card2s;
    }

    public void addCard2(Card2 card2) {
        this.card2s.add(card2);
    }
    public Avatar2 getAvatar2() {
        return avatar2;
    }

    public void setAvatar2(Avatar2 avatar2) {
        this.avatar2 = avatar2;
    }

}