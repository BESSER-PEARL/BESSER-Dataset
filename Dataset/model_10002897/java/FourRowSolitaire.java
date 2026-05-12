





import java.util.List;
import java.util.ArrayList;

public class FourRowSolitaire  {

    private String helpMenu;
    private String appearance;
    private String undo;
    private String help;
    private String game;
    private String newGame;
    private None version;
    private String options;
    private String checkUpdate;
    private String about;
    private String exit;
    private String statistics;
    private String menuBar;
    private String hint;



    public FourRowSolitaire(
        String helpMenu,        String appearance,        String undo,        String help,        String game,        String newGame,        None version,        String options,        String checkUpdate,        String about,        String exit,        String statistics,        String menuBar,        String hint    ) {
        this.helpMenu = helpMenu;
        this.appearance = appearance;
        this.undo = undo;
        this.help = help;
        this.game = game;
        this.newGame = newGame;
        this.version = version;
        this.options = options;
        this.checkUpdate = checkUpdate;
        this.about = about;
        this.exit = exit;
        this.statistics = statistics;
        this.menuBar = menuBar;
        this.hint = hint;
    }


    public String getHelpmenu() {
        return helpMenu;
    }

    public void setHelpmenu(String helpMenu) {
        this.helpMenu = helpMenu;
    }
    public String getAppearance() {
        return appearance;
    }

    public void setAppearance(String appearance) {
        this.appearance = appearance;
    }
    public String getUndo() {
        return undo;
    }

    public void setUndo(String undo) {
        this.undo = undo;
    }
    public String getHelp() {
        return help;
    }

    public void setHelp(String help) {
        this.help = help;
    }
    public String getGame() {
        return game;
    }

    public void setGame(String game) {
        this.game = game;
    }
    public String getNewgame() {
        return newGame;
    }

    public void setNewgame(String newGame) {
        this.newGame = newGame;
    }
    public None getVersion() {
        return version;
    }

    public void setVersion(None version) {
        this.version = version;
    }
    public String getOptions() {
        return options;
    }

    public void setOptions(String options) {
        this.options = options;
    }
    public String getCheckupdate() {
        return checkUpdate;
    }

    public void setCheckupdate(String checkUpdate) {
        this.checkUpdate = checkUpdate;
    }
    public String getAbout() {
        return about;
    }

    public void setAbout(String about) {
        this.about = about;
    }
    public String getExit() {
        return exit;
    }

    public void setExit(String exit) {
        this.exit = exit;
    }
    public String getStatistics() {
        return statistics;
    }

    public void setStatistics(String statistics) {
        this.statistics = statistics;
    }
    public String getMenubar() {
        return menuBar;
    }

    public void setMenubar(String menuBar) {
        this.menuBar = menuBar;
    }
    public String getHint() {
        return hint;
    }

    public void setHint(String hint) {
        this.hint = hint;
    }


}