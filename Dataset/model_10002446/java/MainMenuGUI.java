





import java.util.List;
import java.util.ArrayList;

public class MainMenuGUI  {






    private ScoreBoardGUI scoreboardgui;




    private Connect4GUI connect4gui;


    public MainMenuGUI(
    ) {
    }



    public ScoreBoardGUI getScoreboardgui() {
        return scoreboardgui;
    }

    public void setScoreboardgui(ScoreBoardGUI scoreboardgui) {
        this.scoreboardgui = scoreboardgui;
    }
    public Connect4GUI getConnect4gui() {
        return connect4gui;
    }

    public void setConnect4gui(Connect4GUI connect4gui) {
        this.connect4gui = connect4gui;
    }

}