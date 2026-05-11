





import java.util.List;
import java.util.ArrayList;

public class moba_MobaModelFeature extends MobaFriendsAble {

    private String version;
    private String name;
    private String id;



    public moba_MobaModelFeature(
        String version,        String name,        String id    ) {
        super(
        );
        this.version = version;
        this.name = name;
        this.id = id;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}