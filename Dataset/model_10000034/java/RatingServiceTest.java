





import java.util.List;
import java.util.ArrayList;

public class RatingServiceTest  {

    private String TEST_PLAYER_2;
    private String TEST_PLAYER;
    private String GAME_NAME;
    private String TEST_PLAYER_3;



    public RatingServiceTest(
        String TEST_PLAYER_2,        String TEST_PLAYER,        String GAME_NAME,        String TEST_PLAYER_3    ) {
        this.TEST_PLAYER_2 = TEST_PLAYER_2;
        this.TEST_PLAYER = TEST_PLAYER;
        this.GAME_NAME = GAME_NAME;
        this.TEST_PLAYER_3 = TEST_PLAYER_3;
    }


    public String getTest_player_2() {
        return TEST_PLAYER_2;
    }

    public void setTest_player_2(String TEST_PLAYER_2) {
        this.TEST_PLAYER_2 = TEST_PLAYER_2;
    }
    public String getTest_player() {
        return TEST_PLAYER;
    }

    public void setTest_player(String TEST_PLAYER) {
        this.TEST_PLAYER = TEST_PLAYER;
    }
    public String getGame_name() {
        return GAME_NAME;
    }

    public void setGame_name(String GAME_NAME) {
        this.GAME_NAME = GAME_NAME;
    }
    public String getTest_player_3() {
        return TEST_PLAYER_3;
    }

    public void setTest_player_3(String TEST_PLAYER_3) {
        this.TEST_PLAYER_3 = TEST_PLAYER_3;
    }


}