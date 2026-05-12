





import java.util.List;
import java.util.ArrayList;

public class CommentServiceTest  {

    private String GAME_NAME;
    private String PLAYER_NAME;



    public CommentServiceTest(
        String GAME_NAME,        String PLAYER_NAME    ) {
        this.GAME_NAME = GAME_NAME;
        this.PLAYER_NAME = PLAYER_NAME;
    }


    public String getGame_name() {
        return GAME_NAME;
    }

    public void setGame_name(String GAME_NAME) {
        this.GAME_NAME = GAME_NAME;
    }
    public String getPlayer_name() {
        return PLAYER_NAME;
    }

    public void setPlayer_name(String PLAYER_NAME) {
        this.PLAYER_NAME = PLAYER_NAME;
    }


}