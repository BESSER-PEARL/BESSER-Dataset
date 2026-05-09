





import java.util.List;
import java.util.ArrayList;

public class highlevelnets_npnets_Synchronization extends INetElement {

    private String kind;
    private String key;



    public highlevelnets_npnets_Synchronization(
        String kind,        String key    ) {
        super(
        );
        this.kind = kind;
        this.key = key;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }


}