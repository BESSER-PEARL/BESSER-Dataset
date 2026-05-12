





import java.util.List;
import java.util.ArrayList;

public class Board  {

    private None scores;
    private None board;
    private None boardGui;





    private Game game;


    public Board(
        None scores,        None board,        None boardGui    ) {
        this.scores = scores;
        this.board = board;
        this.boardGui = boardGui;
    }


    public None getScores() {
        return scores;
    }

    public void setScores(None scores) {
        this.scores = scores;
    }
    public None getBoard() {
        return board;
    }

    public void setBoard(None board) {
        this.board = board;
    }
    public None getBoardgui() {
        return boardGui;
    }

    public void setBoardgui(None boardGui) {
        this.boardGui = boardGui;
    }

    public Game getGame() {
        return game;
    }

    public void setGame(Game game) {
        this.game = game;
    }

}