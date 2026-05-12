





import java.util.List;
import java.util.ArrayList;

public class FourRowSolitaire  {

    private String newGame;
    private String checkUpdate;
    private String menuBar;
    private String undo;
    private String about;
    private String statistics;
    private String exit;
    private String help;
    private String options;
    private String game;
    private String hint;
    private String helpMenu;
    private String appearance;
    private None version;



    public FourRowSolitaire(
        String newGame,        String checkUpdate,        String menuBar,        String undo,        String about,        String statistics,        String exit,        String help,        String options,        String game,        String hint,        String helpMenu,        String appearance,        None version    ) {
        this.newGame = newGame;
        this.checkUpdate = checkUpdate;
        this.menuBar = menuBar;
        this.undo = undo;
        this.about = about;
        this.statistics = statistics;
        this.exit = exit;
        this.help = help;
        this.options = options;
        this.game = game;
        this.hint = hint;
        this.helpMenu = helpMenu;
        this.appearance = appearance;
        this.version = version;
    }


    public String getNewgame() {
        return newGame;
    }

    public void setNewgame(String newGame) {
        this.newGame = newGame;
    }
    public String getCheckupdate() {
        return checkUpdate;
    }

    public void setCheckupdate(String checkUpdate) {
        this.checkUpdate = checkUpdate;
    }
    public String getMenubar() {
        return menuBar;
    }

    public void setMenubar(String menuBar) {
        this.menuBar = menuBar;
    }
    public String getUndo() {
        return undo;
    }

    public void setUndo(String undo) {
        this.undo = undo;
    }
    public String getAbout() {
        return about;
    }

    public void setAbout(String about) {
        this.about = about;
    }
    public String getStatistics() {
        return statistics;
    }

    public void setStatistics(String statistics) {
        this.statistics = statistics;
    }
    public String getExit() {
        return exit;
    }

    public void setExit(String exit) {
        this.exit = exit;
    }
    public String getHelp() {
        return help;
    }

    public void setHelp(String help) {
        this.help = help;
    }
    public String getOptions() {
        return options;
    }

    public void setOptions(String options) {
        this.options = options;
    }
    public String getGame() {
        return game;
    }

    public void setGame(String game) {
        this.game = game;
    }
    public String getHint() {
        return hint;
    }

    public void setHint(String hint) {
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
    public None getVersion() {
        return version;
    }

    public void setVersion(None version) {
        this.version = version;
    }


}