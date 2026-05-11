





import java.util.List;
import java.util.ArrayList;

public class bowling_Game  {

    private int frames;





    private bowling_Player bowling_player;


    public bowling_Game(
        int frames    ) {
        this.frames = frames;
    }


    public int getFrames() {
        return frames;
    }

    public void setFrames(int frames) {
        this.frames = frames;
    }

    public bowling_Player getBowling_player() {
        return bowling_player;
    }

    public void setBowling_player(bowling_Player bowling_player) {
        this.bowling_player = bowling_player;
    }

}