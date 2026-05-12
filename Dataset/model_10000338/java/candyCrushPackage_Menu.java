





import java.util.List;
import java.util.ArrayList;

public class candyCrushPackage_Menu  {

    private String buttonBGColor;
    private String highScoreLabel;
    private String menuBGColor;
    private String movesLabel;





    private candyCrushPackage_Game candycrushpackage_game;


    public candyCrushPackage_Menu(
        String buttonBGColor,        String highScoreLabel,        String menuBGColor,        String movesLabel    ) {
        this.buttonBGColor = buttonBGColor;
        this.highScoreLabel = highScoreLabel;
        this.menuBGColor = menuBGColor;
        this.movesLabel = movesLabel;
    }


    public String getButtonbgcolor() {
        return buttonBGColor;
    }

    public void setButtonbgcolor(String buttonBGColor) {
        this.buttonBGColor = buttonBGColor;
    }
    public String getHighscorelabel() {
        return highScoreLabel;
    }

    public void setHighscorelabel(String highScoreLabel) {
        this.highScoreLabel = highScoreLabel;
    }
    public String getMenubgcolor() {
        return menuBGColor;
    }

    public void setMenubgcolor(String menuBGColor) {
        this.menuBGColor = menuBGColor;
    }
    public String getMoveslabel() {
        return movesLabel;
    }

    public void setMoveslabel(String movesLabel) {
        this.movesLabel = movesLabel;
    }

    public candyCrushPackage_Game getCandycrushpackage_game() {
        return candycrushpackage_game;
    }

    public void setCandycrushpackage_game(candyCrushPackage_Game candycrushpackage_game) {
        this.candycrushpackage_game = candycrushpackage_game;
    }

}