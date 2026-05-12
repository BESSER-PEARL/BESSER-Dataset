





import java.util.List;
import java.util.ArrayList;

public class GameBoard  {

    private String board;
    private String score;
    private String selectCard;
    private String startGame;
    private String drawCard;



    public GameBoard(
        String board,        String score,        String selectCard,        String startGame,        String drawCard    ) {
        this.board = board;
        this.score = score;
        this.selectCard = selectCard;
        this.startGame = startGame;
        this.drawCard = drawCard;
    }


    public String getBoard() {
        return board;
    }

    public void setBoard(String board) {
        this.board = board;
    }
    public String getScore() {
        return score;
    }

    public void setScore(String score) {
        this.score = score;
    }
    public String getSelectcard() {
        return selectCard;
    }

    public void setSelectcard(String selectCard) {
        this.selectCard = selectCard;
    }
    public String getStartgame() {
        return startGame;
    }

    public void setStartgame(String startGame) {
        this.startGame = startGame;
    }
    public String getDrawcard() {
        return drawCard;
    }

    public void setDrawcard(String drawCard) {
        this.drawCard = drawCard;
    }


}