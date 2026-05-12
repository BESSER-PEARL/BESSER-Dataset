





import java.util.List;
import java.util.ArrayList;

public class entities_Rating  {

    private String game;
    private None ratedon;
    private int rating;
    private String player;



    public entities_Rating(
        String game,        None ratedon,        int rating,        String player    ) {
        this.game = game;
        this.ratedon = ratedon;
        this.rating = rating;
        this.player = player;
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
    public int getRating() {
        return rating;
    }

    public void setRating(int rating) {
        this.rating = rating;
    }
    public String getPlayer() {
        return player;
    }

    public void setPlayer(String player) {
        this.player = player;
    }


}