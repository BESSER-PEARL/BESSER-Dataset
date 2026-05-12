





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private boolean won;
    private String name;
    private boolean turn;





    private Board board;


    public Player(
        boolean won,        String name,        boolean turn    ) {
        this.won = won;
        this.name = name;
        this.turn = turn;
    }


    public boolean getWon() {
        return won;
    }

    public void setWon(boolean won) {
        this.won = won;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getTurn() {
        return turn;
    }

    public void setTurn(boolean turn) {
        this.turn = turn;
    }

    public Board getBoard() {
        return board;
    }

    public void setBoard(Board board) {
        this.board = board;
    }

}