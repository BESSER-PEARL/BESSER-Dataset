





import java.util.List;
import java.util.ArrayList;

public class eSport_GroupStage  {

    private int maxNbGames;
    private int meetingsWithOtherGroups;
    private String type;
    private int meetingsInSameGroup;





    private eSport_Tournament esport_tournament;




    private eSport_Tournament esport_tournament;


    public eSport_GroupStage(
        int maxNbGames,        int meetingsWithOtherGroups,        String type,        int meetingsInSameGroup    ) {
        this.maxNbGames = maxNbGames;
        this.meetingsWithOtherGroups = meetingsWithOtherGroups;
        this.type = type;
        this.meetingsInSameGroup = meetingsInSameGroup;
    }


    public int getMaxnbgames() {
        return maxNbGames;
    }

    public void setMaxnbgames(int maxNbGames) {
        this.maxNbGames = maxNbGames;
    }
    public int getMeetingswithothergroups() {
        return meetingsWithOtherGroups;
    }

    public void setMeetingswithothergroups(int meetingsWithOtherGroups) {
        this.meetingsWithOtherGroups = meetingsWithOtherGroups;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getMeetingsinsamegroup() {
        return meetingsInSameGroup;
    }

    public void setMeetingsinsamegroup(int meetingsInSameGroup) {
        this.meetingsInSameGroup = meetingsInSameGroup;
    }

    public eSport_Tournament getEsport_tournament() {
        return esport_tournament;
    }

    public void setEsport_tournament(eSport_Tournament esport_tournament) {
        this.esport_tournament = esport_tournament;
    }
    public eSport_Tournament getEsport_tournament() {
        return esport_tournament;
    }

    public void setEsport_tournament(eSport_Tournament esport_tournament) {
        this.esport_tournament = esport_tournament;
    }

}