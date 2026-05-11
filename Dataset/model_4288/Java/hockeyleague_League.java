





import java.util.List;
import java.util.ArrayList;

public class hockeyleague_League extends HockeyleagueObject {

    private String headoffice;





    private List<hockeyleague_Team> hockeyleague_teams;


    public hockeyleague_League(
        String headoffice    ) {
        super(
        );
        this.headoffice = headoffice;
        this.hockeyleague_teams = new ArrayList<>();
    }

    public hockeyleague_League(
        String headoffice        ArrayList<hockeyleague_Team> hockeyleague_teams    ) {
        this.headoffice = headoffice;
        this.hockeyleague_teams = hockeyleague_teams;
    }

    public String getHeadoffice() {
        return headoffice;
    }

    public void setHeadoffice(String headoffice) {
        this.headoffice = headoffice;
    }

    public List<hockeyleague_Team> getHockeyleague_teams() {
        return hockeyleague_teams;
    }

    public void addHockeyleague_team(Hockeyleague_team hockeyleague_team) {
        this.hockeyleague_teams.add(hockeyleague_team);
    }

}