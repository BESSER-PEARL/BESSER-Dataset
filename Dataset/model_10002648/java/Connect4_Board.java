





import java.util.List;
import java.util.ArrayList;

public class Connect4_Board  {

    private int maxColumns;
    private int maxRows;
    private String gameBoard;





    private List<Connect4_Token> connect4_tokens;


    public Connect4_Board(
        int maxColumns,        int maxRows,        String gameBoard    ) {
        this.maxColumns = maxColumns;
        this.maxRows = maxRows;
        this.gameBoard = gameBoard;
        this.connect4_tokens = new ArrayList<>();
    }

    public Connect4_Board(
        int maxColumns,        int maxRows,        String gameBoard        ArrayList<Connect4_Token> connect4_tokens    ) {
        this.maxColumns = maxColumns;
        this.maxRows = maxRows;
        this.gameBoard = gameBoard;
        this.connect4_tokens = connect4_tokens;
    }

    public int getMaxcolumns() {
        return maxColumns;
    }

    public void setMaxcolumns(int maxColumns) {
        this.maxColumns = maxColumns;
    }
    public int getMaxrows() {
        return maxRows;
    }

    public void setMaxrows(int maxRows) {
        this.maxRows = maxRows;
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

}