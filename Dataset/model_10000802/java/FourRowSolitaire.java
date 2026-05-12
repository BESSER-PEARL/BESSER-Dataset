





import java.util.List;
import java.util.ArrayList;

public class FourRowSolitaire  {

    private String version;
    private String helpMenu;
    private String exit;
    private String options;
    private String game;
    private String hint;
    private String help;
    private String newGame;
    private String menubar;
    private String about;
    private String undo;
    private String statistics;
    private String appearance;
    private String checkUpdate;



    public FourRowSolitaire(
        String version,        String helpMenu,        String exit,        String options,        String game,        String hint,        String help,        String newGame,        String menubar,        String about,        String undo,        String statistics,        String appearance,        String checkUpdate    ) {
        this.version = version;
        this.helpMenu = helpMenu;
        this.exit = exit;
        this.options = options;
        this.game = game;
        this.hint = hint;
        this.help = help;
        this.newGame = newGame;
        this.menubar = menubar;
        this.about = about;
        this.undo = undo;
        this.statistics = statistics;
        this.appearance = appearance;
        this.checkUpdate = checkUpdate;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getHelpmenu() {
        return helpMenu;
    }

    public void setHelpmenu(String helpMenu) {
        this.helpMenu = helpMenu;
    }
    public String getExit() {
        return exit;
    }

    public void setExit(String exit) {
        this.exit = exit;
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
    public String getHelp() {
        return help;
    }

    public void setHelp(String help) {
        this.help = help;
    }
    public String getNewgame() {
        return newGame;
    }

    public void setNewgame(String newGame) {
        this.newGame = newGame;
    }
    public String getMenubar() {
        return menubar;
    }

    public void setMenubar(String menubar) {
        this.menubar = menubar;
    }
    public String getAbout() {
        return about;
    }

    public void setAbout(String about) {
        this.about = about;
    }
    public String getUndo() {
        return undo;
    }

    public void setUndo(String undo) {
        this.undo = undo;
    }
    public String getStatistics() {
        return statistics;
    }

    public void setStatistics(String statistics) {
        this.statistics = statistics;
    }
    public String getAppearance() {
        return appearance;
    }

    public void setAppearance(String appearance) {
        this.appearance = appearance;
    }
    public String getCheckupdate() {
        return checkUpdate;
    }

    public void setCheckupdate(String checkUpdate) {
        this.checkUpdate = checkUpdate;
    }


}