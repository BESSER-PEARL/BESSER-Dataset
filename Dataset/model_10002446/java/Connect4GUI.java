





import java.util.List;
import java.util.ArrayList;

public class Connect4GUI  {

    private String root;
    private None undo;





    private GameboardGUI gameboardgui;


    public Connect4GUI(
        String root,        None undo    ) {
        this.root = root;
        this.undo = undo;
    }


    public String getRoot() {
        return root;
    }

    public void setRoot(String root) {
        this.root = root;
    }
    public None getUndo() {
        return undo;
    }

    public void setUndo(None undo) {
        this.undo = undo;
    }

    public GameboardGUI getGameboardgui() {
        return gameboardgui;
    }

    public void setGameboardgui(GameboardGUI gameboardgui) {
        this.gameboardgui = gameboardgui;
    }

}