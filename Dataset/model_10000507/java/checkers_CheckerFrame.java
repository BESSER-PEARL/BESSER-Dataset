





import java.util.List;
import java.util.ArrayList;

public class checkers_CheckerFrame  {

    private String startButton;
    private String gamePanel;



    public checkers_CheckerFrame(
        String startButton,        String gamePanel    ) {
        this.startButton = startButton;
        this.gamePanel = gamePanel;
    }


    public String getStartbutton() {
        return startButton;
    }

    public void setStartbutton(String startButton) {
        this.startButton = startButton;
    }
    public String getGamepanel() {
        return gamePanel;
    }

    public void setGamepanel(String gamePanel) {
        this.gamePanel = gamePanel;
    }


}