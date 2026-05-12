





import java.util.List;
import java.util.ArrayList;

public class entities_Comment  {

    private String player;
    private String comment;
    private None commentedOn;
    private String game;



    public entities_Comment(
        String player,        String comment,        None commentedOn,        String game    ) {
        this.player = player;
        this.comment = comment;
        this.commentedOn = commentedOn;
        this.game = game;
    }


    public String getPlayer() {
        return player;
    }

    public void setPlayer(String player) {
        this.player = player;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public None getCommentedon() {
        return commentedOn;
    }

    public void setCommentedon(None commentedOn) {
        this.commentedOn = commentedOn;
    }
    public String getGame() {
        return game;
    }

    public void setGame(String game) {
        this.game = game;
    }


}