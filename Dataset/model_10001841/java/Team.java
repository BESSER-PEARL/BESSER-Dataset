





import java.util.List;
import java.util.ArrayList;

public class Team  {

    private String Ministry;
    private None Robotric_teams;
    private None Footballs_teams;
    private String President;





    private Students students;


    public Team(
        String Ministry,        None Robotric_teams,        None Footballs_teams,        String President    ) {
        this.Ministry = Ministry;
        this.Robotric_teams = Robotric_teams;
        this.Footballs_teams = Footballs_teams;
        this.President = President;
    }


    public String getMinistry() {
        return Ministry;
    }

    public void setMinistry(String Ministry) {
        this.Ministry = Ministry;
    }
    public None getRobotric_teams() {
        return Robotric_teams;
    }

    public void setRobotric_teams(None Robotric_teams) {
        this.Robotric_teams = Robotric_teams;
    }
    public None getFootballs_teams() {
        return Footballs_teams;
    }

    public void setFootballs_teams(None Footballs_teams) {
        this.Footballs_teams = Footballs_teams;
    }
    public String getPresident() {
        return President;
    }

    public void setPresident(String President) {
        this.President = President;
    }

    public Students getStudents() {
        return students;
    }

    public void setStudents(Students students) {
        this.students = students;
    }

}