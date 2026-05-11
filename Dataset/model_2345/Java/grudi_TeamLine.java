





import java.util.List;
import java.util.ArrayList;

public class grudi_TeamLine  {

    private String kind;
    private String id;
    private String versionNumber;





    private grudi_Team grudi_team;




    private grudi_PersonInfo grudi_personinfo;




    private grudi_Team grudi_team;


    public grudi_TeamLine(
        String kind,        String id,        String versionNumber    ) {
        this.kind = kind;
        this.id = id;
        this.versionNumber = versionNumber;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getVersionnumber() {
        return versionNumber;
    }

    public void setVersionnumber(String versionNumber) {
        this.versionNumber = versionNumber;
    }

    public grudi_Team getGrudi_team() {
        return grudi_team;
    }

    public void setGrudi_team(grudi_Team grudi_team) {
        this.grudi_team = grudi_team;
    }
    public grudi_PersonInfo getGrudi_personinfo() {
        return grudi_personinfo;
    }

    public void setGrudi_personinfo(grudi_PersonInfo grudi_personinfo) {
        this.grudi_personinfo = grudi_personinfo;
    }
    public grudi_Team getGrudi_team() {
        return grudi_team;
    }

    public void setGrudi_team(grudi_Team grudi_team) {
        this.grudi_team = grudi_team;
    }

}