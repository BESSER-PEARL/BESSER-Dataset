





import java.util.List;
import java.util.ArrayList;

public class entities_Rating  {

    private int rating;
    private String game;
    private None ratedon;
    private String player;



    public entities_Rating(
        int rating,        String game,        None ratedon,        String player    ) {
        this.rating = rating;
        this.game = game;
        this.ratedon = ratedon;
        this.player = player;
    }


    public int getRating() {
        return rating;
    }

    public void setRating(int rating) {
        this.rating = rating;
    }
    public String getGame() {
        return game;
    }

    public void setGame(String game) {
        this.game = game;
    }
    public None getRatedon() {
        return ratedon;
    }

    public void setRatedon(None ratedon) {
        this.ratedon = ratedon;
    }
    public String getPlayer() {
        return player;
    }

    public void setPlayer(String player) {
        this.player = player;
    }


}