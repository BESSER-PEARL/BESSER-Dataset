





import java.util.List;
import java.util.ArrayList;

public class entities_Comment  {

    private String comment;
    private None commentedOn;
    private String player;
    private String game;



    public entities_Comment(
        String comment,        None commentedOn,        String player,        String game    ) {
        this.comment = comment;
        this.commentedOn = commentedOn;
        this.player = player;
        this.game = game;
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
    public String getPlayer() {
        return player;
    }

    public void setPlayer(String player) {
        this.player = player;
    }
    public String getGame() {
        return game;
    }

    public void setGame(String game) {
        this.game = game;
    }


}