





import java.util.List;
import java.util.ArrayList;

public class Board  {

    private None currentPlayer;
    private String spots;
    private boolean isCheck;
    private boolean isStaleMate;
    private boolean isCheckMate;
    private None whitePlayer;
    private None blackPlayer;



    public Board(
        None currentPlayer,        String spots,        boolean isCheck,        boolean isStaleMate,        boolean isCheckMate,        None whitePlayer,        None blackPlayer    ) {
        this.currentPlayer = currentPlayer;
        this.spots = spots;
        this.isCheck = isCheck;
        this.isStaleMate = isStaleMate;
        this.isCheckMate = isCheckMate;
        this.whitePlayer = whitePlayer;
        this.blackPlayer = blackPlayer;
    }


    public None getCurrentplayer() {
        return currentPlayer;
    }

    public void setCurrentplayer(None currentPlayer) {
        this.currentPlayer = currentPlayer;
    }
    public String getSpots() {
        return spots;
    }

    public void setSpots(String spots) {
        this.spots = spots;
    }
    public boolean getIscheck() {
        return isCheck;
    }

    public void setIscheck(boolean isCheck) {
        this.isCheck = isCheck;
    }
    public boolean getIsstalemate() {
        return isStaleMate;
    }

    public void setIsstalemate(boolean isStaleMate) {
        this.isStaleMate = isStaleMate;
    }
    public boolean getIscheckmate() {
        return isCheckMate;
    }

    public void setIscheckmate(boolean isCheckMate) {
        this.isCheckMate = isCheckMate;
    }
    public None getWhiteplayer() {
        return whitePlayer;
    }

    public void setWhiteplayer(None whitePlayer) {
        this.whitePlayer = whitePlayer;
    }
    public None getBlackplayer() {
        return blackPlayer;
    }

    public void setBlackplayer(None blackPlayer) {
        this.blackPlayer = blackPlayer;
    }


}