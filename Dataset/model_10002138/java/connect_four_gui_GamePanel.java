





import java.util.List;
import java.util.ArrayList;

public class connect_four_gui_GamePanel  {

    private String pieces;
    private int whoPlayed;
    private None Connect4_GUI;
    private int columnNum;
    private String game;
    private String startUp;
    private boolean isComputerEnabled;
    private String board;
    private String players;
    private String windows;
    private int turnNum;
    private int newDrawPos;
    private boolean justWon;
    private int newColumnNum;



    public connect_four_gui_GamePanel(
        String pieces,        int whoPlayed,        None Connect4_GUI,        int columnNum,        String game,        String startUp,        boolean isComputerEnabled,        String board,        String players,        String windows,        int turnNum,        int newDrawPos,        boolean justWon,        int newColumnNum    ) {
        this.pieces = pieces;
        this.whoPlayed = whoPlayed;
        this.Connect4_GUI = Connect4_GUI;
        this.columnNum = columnNum;
        this.game = game;
        this.startUp = startUp;
        this.isComputerEnabled = isComputerEnabled;
        this.board = board;
        this.players = players;
        this.windows = windows;
        this.turnNum = turnNum;
        this.newDrawPos = newDrawPos;
        this.justWon = justWon;
        this.newColumnNum = newColumnNum;
    }


    public String getPieces() {
        return pieces;
    }

    public void setPieces(String pieces) {
        this.pieces = pieces;
    }
    public int getWhoplayed() {
        return whoPlayed;
    }

    public void setWhoplayed(int whoPlayed) {
        this.whoPlayed = whoPlayed;
    }
    public None getConnect4_gui() {
        return Connect4_GUI;
    }

    public void setConnect4_gui(None Connect4_GUI) {
        this.Connect4_GUI = Connect4_GUI;
    }
    public int getColumnnum() {
        return columnNum;
    }

    public void setColumnnum(int columnNum) {
        this.columnNum = columnNum;
    }
    public String getGame() {
        return game;
    }

    public void setGame(String game) {
        this.game = game;
    }
    public String getStartup() {
        return startUp;
    }

    public void setStartup(String startUp) {
        this.startUp = startUp;
    }
    public boolean getIscomputerenabled() {
        return isComputerEnabled;
    }

    public void setIscomputerenabled(boolean isComputerEnabled) {
        this.isComputerEnabled = isComputerEnabled;
    }
    public String getBoard() {
        return board;
    }

    public void setBoard(String board) {
        this.board = board;
    }
    public String getPlayers() {
        return players;
    }

    public void setPlayers(String players) {
        this.players = players;
    }
    public String getWindows() {
        return windows;
    }

    public void setWindows(String windows) {
        this.windows = windows;
    }
    public int getTurnnum() {
        return turnNum;
    }

    public void setTurnnum(int turnNum) {
        this.turnNum = turnNum;
    }
    public int getNewdrawpos() {
        return newDrawPos;
    }

    public void setNewdrawpos(int newDrawPos) {
        this.newDrawPos = newDrawPos;
    }
    public boolean getJustwon() {
        return justWon;
    }

    public void setJustwon(boolean justWon) {
        this.justWon = justWon;
    }
    public int getNewcolumnnum() {
        return newColumnNum;
    }

    public void setNewcolumnnum(int newColumnNum) {
        this.newColumnNum = newColumnNum;
    }


}