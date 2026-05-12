





import java.util.List;
import java.util.ArrayList;

public class Connect4_Board  {

    private int maxRows;
    private int maxColumns;
    private String gameBoard;





    private List<Connect4_Token> connect4_tokens;




    private List<Connect4_Player> connect4_players;


    public Connect4_Board(
        int maxRows,        int maxColumns,        String gameBoard    ) {
        this.maxRows = maxRows;
        this.maxColumns = maxColumns;
        this.gameBoard = gameBoard;
        this.connect4_tokens = new ArrayList<>();
        this.connect4_players = new ArrayList<>();
    }

    public Connect4_Board(
        int maxRows,        int maxColumns,        String gameBoard        ArrayList<Connect4_Token> connect4_tokens,        ArrayList<Connect4_Player> connect4_players    ) {
        this.maxRows = maxRows;
        this.maxColumns = maxColumns;
        this.gameBoard = gameBoard;
        this.connect4_tokens = connect4_tokens;
        this.connect4_players = connect4_players;
    }

    public int getMaxrows() {
        return maxRows;
    }

    public void setMaxrows(int maxRows) {
        this.maxRows = maxRows;
    }
    public int getMaxcolumns() {
        return maxColumns;
    }

    public void setMaxcolumns(int maxColumns) {
        this.maxColumns = maxColumns;
    }
    public String getGameboard() {
        return gameBoard;
    }

    public void setGameboard(String gameBoard) {
        this.gameBoard = gameBoard;
    }

    public List<Connect4_Token> getConnect4_tokens() {
        return connect4_tokens;
    }

    public void addConnect4_token(Connect4_token connect4_token) {
        this.connect4_tokens.add(connect4_token);
    }
    public List<Connect4_Player> getConnect4_players() {
        return connect4_players;
    }

    public void addConnect4_player(Connect4_player connect4_player) {
        this.connect4_players.add(connect4_player);
    }

}