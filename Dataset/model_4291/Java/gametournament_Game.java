





import java.util.List;
import java.util.ArrayList;

public class gametournament_Game  {

    private String name;
    private String type;





    private gametournament_Tournament gametournament_tournament;


    public gametournament_Game(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public gametournament_Tournament getGametournament_tournament() {
        return gametournament_tournament;
    }

    public void setGametournament_tournament(gametournament_Tournament gametournament_tournament) {
        this.gametournament_tournament = gametournament_tournament;
    }

}