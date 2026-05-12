





import java.util.List;
import java.util.ArrayList;

public class Connect4_Board  {

    private String gameBoard;
    private int maxRows;
    private int maxColumns;





    private List<Connect4_Player> connect4_players;




    private List<Connect4_Token> connect4_tokens;


    public Connect4_Board(
        String gameBoard,        int maxRows,        int maxColumns    ) {
        this.gameBoard = gameBoard;
        this.maxRows = maxRows;
        this.maxColumns = maxColumns;
        this.connect4_players = new ArrayList<>();
        this.connect4_tokens = new ArrayList<>();
    }

    public Connect4_Board(
        String gameBoard,        int maxRows,        int maxColumns        ArrayList<Connect4_Player> connect4_players,        ArrayList<Connect4_Token> connect4_tokens    ) {
        this.gameBoard = gameBoard;
        this.maxRows = maxRows;
        this.maxColumns = maxColumns;
        this.connect4_players = connect4_players;
        this.connect4_tokens = connect4_tokens;
    }

    public String getGameboard() {
        return gameBoard;
    }

    public void setGameboard(String gameBoard) {
        this.gameBoard = gameBoard;
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

    public List<Connect4_Player> getConnect4_players() {
        return connect4_players;
    }

    public void addConnect4_player(Connect4_player connect4_player) {
        this.connect4_players.add(connect4_player);
    }
    public List<Connect4_Token> getConnect4_tokens() {
        return connect4_tokens;
    }

    public void addConnect4_token(Connect4_token connect4_token) {
        this.connect4_tokens.add(connect4_token);
    }

}