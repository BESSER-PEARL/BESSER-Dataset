





import java.util.List;
import java.util.ArrayList;

public class Board1  {

    private int boardSize;





    private FreeParking freeparking;




    private List<Player> players;


    public Board1(
        int boardSize    ) {
        this.boardSize = boardSize;
        this.players = new ArrayList<>();
    }

    public Board1(
        int boardSize        ArrayList<Player> players    ) {
        this.boardSize = boardSize;
        this.players = players;
    }

    public int getBoardsize() {
        return boardSize;
    }

    public void setBoardsize(int boardSize) {
        this.boardSize = boardSize;
    }

    public FreeParking getFreeparking() {
        return freeparking;
    }

    public void setFreeparking(FreeParking freeparking) {
        this.freeparking = freeparking;
    }
    public List<Player> getPlayers() {
        return players;
    }

    public void addPlayer(Player player) {
        this.players.add(player);
    }

}