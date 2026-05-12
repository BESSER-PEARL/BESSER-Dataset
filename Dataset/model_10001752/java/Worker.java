





import java.util.List;
import java.util.ArrayList;

public class Worker  {

    private int team;
    private String section;



    public Worker(
        int team,        String section    ) {
        this.team = team;
        this.section = section;
    }


    public int getTeam() {
        return team;
    }

    public void setTeam(int team) {
        this.team = team;
    }
    public String getSection() {
        return section;
    }

    public void setSection(String section) {
        this.section = section;
    }


}