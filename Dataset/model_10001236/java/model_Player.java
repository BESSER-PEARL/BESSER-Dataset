





import java.util.List;
import java.util.ArrayList;

public class model_Player  {

    private int g_maxScore;





    private List<model_Card> model_cards;




    private model_Game model_game;


    public model_Player(
        int g_maxScore    ) {
        this.g_maxScore = g_maxScore;
        this.model_cards = new ArrayList<>();
    }

    public model_Player(
        int g_maxScore        ArrayList<model_Card> model_cards    ) {
        this.g_maxScore = g_maxScore;
        this.model_cards = model_cards;
    }

    public int getG_maxscore() {
        return g_maxScore;
    }

    public void setG_maxscore(int g_maxScore) {
        this.g_maxScore = g_maxScore;
    }

    public List<model_Card> getModel_cards() {
        return model_cards;
    }

    public void addModel_card(Model_card model_card) {
        this.model_cards.add(model_card);
    }
    public model_Game getModel_game() {
        return model_game;
    }

    public void setModel_game(model_Game model_game) {
        this.model_game = model_game;
    }

}