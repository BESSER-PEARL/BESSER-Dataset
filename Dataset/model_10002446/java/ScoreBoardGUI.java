





import java.util.List;
import java.util.ArrayList;

public class ScoreBoardGUI  {

    private String playersList;





    private List<Player_Interface> player_interfaces;


    public ScoreBoardGUI(
        String playersList    ) {
        this.playersList = playersList;
        this.player_interfaces = new ArrayList<>();
    }

    public ScoreBoardGUI(
        String playersList        ArrayList<Player_Interface> player_interfaces    ) {
        this.playersList = playersList;
        this.player_interfaces = player_interfaces;
    }

    public String getPlayerslist() {
        return playersList;
    }

    public void setPlayerslist(String playersList) {
        this.playersList = playersList;
    }

    public List<Player_Interface> getPlayer_interfaces() {
        return player_interfaces;
    }

    public void addPlayer_interface(Player_interface player_interface) {
        this.player_interfaces.add(player_interface);
    }

}