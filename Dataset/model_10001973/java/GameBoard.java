





import java.util.List;
import java.util.ArrayList;

public class GameBoard  {

    private None player1;
    private String whoPlay;
    private String board;
    private None player2;





    private List<Player_Interface> player_interfaces;




    private Connect4GUI connect4gui;


    public GameBoard(
        None player1,        String whoPlay,        String board,        None player2    ) {
        this.player1 = player1;
        this.whoPlay = whoPlay;
        this.board = board;
        this.player2 = player2;
        this.player_interfaces = new ArrayList<>();
    }

    public GameBoard(
        None player1,        String whoPlay,        String board,        None player2        ArrayList<Player_Interface> player_interfaces    ) {
        this.player1 = player1;
        this.whoPlay = whoPlay;
        this.board = board;
        this.player2 = player2;
        this.player_interfaces = player_interfaces;
    }

    public None getPlayer1() {
        return player1;
    }

    public void setPlayer1(None player1) {
        this.player1 = player1;
    }
    public String getWhoplay() {
        return whoPlay;
    }

    public void setWhoplay(String whoPlay) {
        this.whoPlay = whoPlay;
    }
    public String getBoard() {
        return board;
    }

    public void setBoard(String board) {
        this.board = board;
    }
    public None getPlayer2() {
        return player2;
    }

    public void setPlayer2(None player2) {
        this.player2 = player2;
    }

    public List<Player_Interface> getPlayer_interfaces() {
        return player_interfaces;
    }

    public void addPlayer_interface(Player_interface player_interface) {
        this.player_interfaces.add(player_interface);
    }
    public Connect4GUI getConnect4gui() {
        return connect4gui;
    }

    public void setConnect4gui(Connect4GUI connect4gui) {
        this.connect4gui = connect4gui;
    }

}