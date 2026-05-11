





import java.util.List;
import java.util.ArrayList;

public class hockeyleague_Defence extends Player {

    private String position;





    private hockeyleague_Team hockeyleague_team;


    public hockeyleague_Defence(
        String position    ) {
        super(
        );
        this.position = position;
    }


    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }

    public hockeyleague_Team getHockeyleague_team() {
        return hockeyleague_team;
    }

    public void setHockeyleague_team(hockeyleague_Team hockeyleague_team) {
        this.hockeyleague_team = hockeyleague_team;
    }

}