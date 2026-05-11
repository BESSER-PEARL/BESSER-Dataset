





import java.util.List;
import java.util.ArrayList;

public class bowlingTournament_Tournament  {

    private String type;





    private List<bowlingTournament_League> bowlingtournament_leagues;


    public bowlingTournament_Tournament(
        String type    ) {
        this.type = type;
        this.bowlingtournament_leagues = new ArrayList<>();
    }

    public bowlingTournament_Tournament(
        String type        ArrayList<bowlingTournament_League> bowlingtournament_leagues    ) {
        this.type = type;
        this.bowlingtournament_leagues = bowlingtournament_leagues;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<bowlingTournament_League> getBowlingtournament_leagues() {
        return bowlingtournament_leagues;
    }

    public void addBowlingtournament_league(Bowlingtournament_league bowlingtournament_league) {
        this.bowlingtournament_leagues.add(bowlingtournament_league);
    }

}