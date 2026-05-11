





import java.util.List;
import java.util.ArrayList;

public class pokerleague_DataStructureVersion extends Serializable {

    private String currentVersion;
    private int id;



    public pokerleague_DataStructureVersion(
        String currentVersion,        int id    ) {
        super(
        );
        this.currentVersion = currentVersion;
        this.id = id;
    }


    public String getCurrentversion() {
        return currentVersion;
    }

    public void setCurrentversion(String currentVersion) {
        this.currentVersion = currentVersion;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}