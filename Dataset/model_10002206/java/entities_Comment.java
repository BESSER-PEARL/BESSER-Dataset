





import java.util.List;
import java.util.ArrayList;

public class entities_Comment  {

    private String comment;
    private String game;
    private None commentedOn;
    private String player;



    public entities_Comment(
        String comment,        String game,        None commentedOn,        String player    ) {
        this.comment = comment;
        this.game = game;
        this.commentedOn = commentedOn;
        this.player = player;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getGame() {
        return game;
    }

    public void setGame(String game) {
        this.game = game;
    }
    public None getCommentedon() {
        return commentedOn;
    }

    public void setCommentedon(None commentedOn) {
        this.commentedOn = commentedOn;
    }
    public String getPlayer() {
        return player;
    }

    public void setPlayer(String player) {
        this.player = player;
    }


}