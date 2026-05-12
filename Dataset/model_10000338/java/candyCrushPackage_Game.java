





import java.util.List;
import java.util.ArrayList;

public class candyCrushPackage_Game  {

    private String SOUNDS_PATH;
    private String SEP;
    private String playerName;
    private int score;
    private int WINDOW_HEIGHT;
    private int WINDOW_WIDTH;
    private String IMAGES_PATH;



    public candyCrushPackage_Game(
        String SOUNDS_PATH,        String SEP,        String playerName,        int score,        int WINDOW_HEIGHT,        int WINDOW_WIDTH,        String IMAGES_PATH    ) {
        this.SOUNDS_PATH = SOUNDS_PATH;
        this.SEP = SEP;
        this.playerName = playerName;
        this.score = score;
        this.WINDOW_HEIGHT = WINDOW_HEIGHT;
        this.WINDOW_WIDTH = WINDOW_WIDTH;
        this.IMAGES_PATH = IMAGES_PATH;
    }


    public String getSounds_path() {
        return SOUNDS_PATH;
    }

    public void setSounds_path(String SOUNDS_PATH) {
        this.SOUNDS_PATH = SOUNDS_PATH;
    }
    public String getSep() {
        return SEP;
    }

    public void setSep(String SEP) {
        this.SEP = SEP;
    }
    public String getPlayername() {
        return playerName;
    }

    public void setPlayername(String playerName) {
        this.playerName = playerName;
    }
    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }
    public int getWindow_height() {
        return WINDOW_HEIGHT;
    }

    public void setWindow_height(int WINDOW_HEIGHT) {
        this.WINDOW_HEIGHT = WINDOW_HEIGHT;
    }
    public int getWindow_width() {
        return WINDOW_WIDTH;
    }

    public void setWindow_width(int WINDOW_WIDTH) {
        this.WINDOW_WIDTH = WINDOW_WIDTH;
    }
    public String getImages_path() {
        return IMAGES_PATH;
    }

    public void setImages_path(String IMAGES_PATH) {
        this.IMAGES_PATH = IMAGES_PATH;
    }


}