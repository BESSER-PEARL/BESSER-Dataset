





import java.util.List;
import java.util.ArrayList;

public class BlackJack_Game  {

    private boolean win_loose;





    private List<BlackJack_Player> blackjack_players;




    private BlackJack_House blackjack_house;


    public BlackJack_Game(
        boolean win_loose    ) {
        this.win_loose = win_loose;
        this.blackjack_players = new ArrayList<>();
    }

    public BlackJack_Game(
        boolean win_loose        ArrayList<BlackJack_Player> blackjack_players    ) {
        this.win_loose = win_loose;
        this.blackjack_players = blackjack_players;
    }

    public boolean getWin_loose() {
        return win_loose;
    }

    public void setWin_loose(boolean win_loose) {
        this.win_loose = win_loose;
    }

    public List<BlackJack_Player> getBlackjack_players() {
        return blackjack_players;
    }

    public void addBlackjack_player(Blackjack_player blackjack_player) {
        this.blackjack_players.add(blackjack_player);
    }
    public BlackJack_House getBlackjack_house() {
        return blackjack_house;
    }

    public void setBlackjack_house(BlackJack_House blackjack_house) {
        this.blackjack_house = blackjack_house;
    }

}