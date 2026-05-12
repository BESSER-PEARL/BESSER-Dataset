





import java.util.List;
import java.util.ArrayList;

public class connect_four_gui_Connect4GUI  {

    private None cpList;
    private String startUp;
    private boolean comp;
    private boolean redToken;
    private String tokenRoot;
    private String gridBoard;
    private String window;





    private connect_four_gui_GamePanel connect_four_gui_gamepanel;


    public connect_four_gui_Connect4GUI(
        None cpList,        String startUp,        boolean comp,        boolean redToken,        String tokenRoot,        String gridBoard,        String window    ) {
        this.cpList = cpList;
        this.startUp = startUp;
        this.comp = comp;
        this.redToken = redToken;
        this.tokenRoot = tokenRoot;
        this.gridBoard = gridBoard;
        this.window = window;
    }


    public None getCplist() {
        return cpList;
    }

    public void setCplist(None cpList) {
        this.cpList = cpList;
    }
    public String getStartup() {
        return startUp;
    }

    public void setStartup(String startUp) {
        this.startUp = startUp;
    }
    public boolean getComp() {
        return comp;
    }

    public void setComp(boolean comp) {
        this.comp = comp;
    }
    public boolean getRedtoken() {
        return redToken;
    }

    public void setRedtoken(boolean redToken) {
        this.redToken = redToken;
    }
    public String getTokenroot() {
        return tokenRoot;
    }

    public void setTokenroot(String tokenRoot) {
        this.tokenRoot = tokenRoot;
    }
    public String getGridboard() {
        return gridBoard;
    }

    public void setGridboard(String gridBoard) {
        this.gridBoard = gridBoard;
    }
    public String getWindow() {
        return window;
    }

    public void setWindow(String window) {
        this.window = window;
    }

    public connect_four_gui_GamePanel getConnect_four_gui_gamepanel() {
        return connect_four_gui_gamepanel;
    }

    public void setConnect_four_gui_gamepanel(connect_four_gui_GamePanel connect_four_gui_gamepanel) {
        this.connect_four_gui_gamepanel = connect_four_gui_gamepanel;
    }

}