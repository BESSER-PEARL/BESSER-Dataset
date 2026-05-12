





import java.util.List;
import java.util.ArrayList;

public class BoardGUI  {

    private None frame;





    private Board1 board1;




    private List<PlayerIcon> playericons;


    public BoardGUI(
        None frame    ) {
        this.frame = frame;
        this.playericons = new ArrayList<>();
    }

    public BoardGUI(
        None frame        ArrayList<PlayerIcon> playericons    ) {
        this.frame = frame;
        this.playericons = playericons;
    }

    public None getFrame() {
        return frame;
    }

    public void setFrame(None frame) {
        this.frame = frame;
    }

    public Board1 getBoard1() {
        return board1;
    }

    public void setBoard1(Board1 board1) {
        this.board1 = board1;
    }
    public List<PlayerIcon> getPlayericons() {
        return playericons;
    }

    public void addPlayericon(Playericon playericon) {
        this.playericons.add(playericon);
    }

}