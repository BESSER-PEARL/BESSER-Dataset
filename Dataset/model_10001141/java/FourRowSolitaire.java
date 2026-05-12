





import java.util.List;
import java.util.ArrayList;

public class FourRowSolitaire  {

    private String about;
    private String appearance;
    private String helpMenu;
    private String options;
    private String game;
    private String hint;
    private String exit;
    private String checkUpdate;
    private String newGame;
    private String undo;
    private String menubar;
    private String help;
    private String version;
    private String statistics;



    public FourRowSolitaire(
        String about,        String appearance,        String helpMenu,        String options,        String game,        String hint,        String exit,        String checkUpdate,        String newGame,        String undo,        String menubar,        String help,        String version,        String statistics    ) {
        this.about = about;
        this.appearance = appearance;
        this.helpMenu = helpMenu;
        this.options = options;
        this.game = game;
        this.hint = hint;
        this.exit = exit;
        this.checkUpdate = checkUpdate;
        this.newGame = newGame;
        this.undo = undo;
        this.menubar = menubar;
        this.help = help;
        this.version = version;
        this.statistics = statistics;
    }


    public String getAbout() {
        return about;
    }

    public void setAbout(String about) {
        this.about = about;
    }
    public String getAppearance() {
        return appearance;
    }

    public void setAppearance(String appearance) {
        this.appearance = appearance;
    }
    public String getHelpmenu() {
        return helpMenu;
    }

    public void setHelpmenu(String helpMenu) {
        this.helpMenu = helpMenu;
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
    public String getExit() {
        return exit;
    }

    public void setExit(String exit) {
        this.exit = exit;
    }
    public String getCheckupdate() {
        return checkUpdate;
    }

    public void setCheckupdate(String checkUpdate) {
        this.checkUpdate = checkUpdate;
    }
    public String getNewgame() {
        return newGame;
    }

    public void setNewgame(String newGame) {
        this.newGame = newGame;
    }
    public String getUndo() {
        return undo;
    }

    public void setUndo(String undo) {
        this.undo = undo;
    }
    public String getMenubar() {
        return menubar;
    }

    public void setMenubar(String menubar) {
        this.menubar = menubar;
    }
    public String getHelp() {
        return help;
    }

    public void setHelp(String help) {
        this.help = help;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getStatistics() {
        return statistics;
    }

    public void setStatistics(String statistics) {
        this.statistics = statistics;
    }


}