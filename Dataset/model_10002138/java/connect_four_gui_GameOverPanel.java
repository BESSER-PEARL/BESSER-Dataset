





import java.util.List;
import java.util.ArrayList;

public class connect_four_gui_GameOverPanel  {

    private String labelGameOVer;
    private None butPlayAgain;
    private None butMainMenu;
    private String winnerDisplay;
    private None gui;
    private String winner;





    private connect_four_gui_Connect4GUI connect_four_gui_connect4gui;


    public connect_four_gui_GameOverPanel(
        String labelGameOVer,        None butPlayAgain,        None butMainMenu,        String winnerDisplay,        None gui,        String winner    ) {
        this.labelGameOVer = labelGameOVer;
        this.butPlayAgain = butPlayAgain;
        this.butMainMenu = butMainMenu;
        this.winnerDisplay = winnerDisplay;
        this.gui = gui;
        this.winner = winner;
    }


    public String getLabelgameover() {
        return labelGameOVer;
    }

    public void setLabelgameover(String labelGameOVer) {
        this.labelGameOVer = labelGameOVer;
    }
    public None getButplayagain() {
        return butPlayAgain;
    }

    public void setButplayagain(None butPlayAgain) {
        this.butPlayAgain = butPlayAgain;
    }
    public None getButmainmenu() {
        return butMainMenu;
    }

    public void setButmainmenu(None butMainMenu) {
        this.butMainMenu = butMainMenu;
    }
    public String getWinnerdisplay() {
        return winnerDisplay;
    }

    public void setWinnerdisplay(String winnerDisplay) {
        this.winnerDisplay = winnerDisplay;
    }
    public None getGui() {
        return gui;
    }

    public void setGui(None gui) {
        this.gui = gui;
    }
    public String getWinner() {
        return winner;
    }

    public void setWinner(String winner) {
        this.winner = winner;
    }

    public connect_four_gui_Connect4GUI getConnect_four_gui_connect4gui() {
        return connect_four_gui_connect4gui;
    }

    public void setConnect_four_gui_connect4gui(connect_four_gui_Connect4GUI connect_four_gui_connect4gui) {
        this.connect_four_gui_connect4gui = connect_four_gui_connect4gui;
    }

}