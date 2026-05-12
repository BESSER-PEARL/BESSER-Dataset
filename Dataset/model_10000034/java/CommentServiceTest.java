





import java.util.List;
import java.util.ArrayList;

public class CommentServiceTest  {

    private String PLAYER_NAME;
    private String GAME_NAME;



    public CommentServiceTest(
        String PLAYER_NAME,        String GAME_NAME    ) {
        this.PLAYER_NAME = PLAYER_NAME;
        this.GAME_NAME = GAME_NAME;
    }


    public String getPlayer_name() {
        return PLAYER_NAME;
    }

    public void setPlayer_name(String PLAYER_NAME) {
        this.PLAYER_NAME = PLAYER_NAME;
    }
    public String getGame_name() {
        return GAME_NAME;
    }

    public void setGame_name(String GAME_NAME) {
        this.GAME_NAME = GAME_NAME;
    }


}