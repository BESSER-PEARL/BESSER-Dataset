





import java.util.List;
import java.util.ArrayList;

public class entities_Rating  {

    private String game;
    private int rating;
    private None ratedon;
    private String player;



    public entities_Rating(
        String game,        int rating,        None ratedon,        String player    ) {
        this.game = game;
        this.rating = rating;
        this.ratedon = ratedon;
        this.player = player;
    }


    public String getGame() {
        return game;
    }

    public void setGame(String game) {
        this.game = game;
    }
    public int getRating() {
        return rating;
    }

    public void setRating(int rating) {
        this.rating = rating;
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