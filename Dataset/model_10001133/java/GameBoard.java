





import java.util.List;
import java.util.ArrayList;

public class GameBoard  {

    private String score;
    private String selectCard;
    private String board;
    private String drawCard;
    private String startGame;



    public GameBoard(
        String score,        String selectCard,        String board,        String drawCard,        String startGame    ) {
        this.score = score;
        this.selectCard = selectCard;
        this.board = board;
        this.drawCard = drawCard;
        this.startGame = startGame;
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
    public String getBoard() {
        return board;
    }

    public void setBoard(String board) {
        this.board = board;
    }
    public String getDrawcard() {
        return drawCard;
    }

    public void setDrawcard(String drawCard) {
        this.drawCard = drawCard;
    }
    public String getStartgame() {
        return startGame;
    }

    public void setStartgame(String startGame) {
        this.startGame = startGame;
    }


}