





import java.util.List;
import java.util.ArrayList;

public class pokerleague_DataVersion extends Serializable {

    private int id;
    private String currentVersion;



    public pokerleague_DataVersion(
        int id,        String currentVersion    ) {
        super(
        );
        this.id = id;
        this.currentVersion = currentVersion;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getCurrentversion() {
        return currentVersion;
    }

    public void setCurrentversion(String currentVersion) {
        this.currentVersion = currentVersion;
    }


}