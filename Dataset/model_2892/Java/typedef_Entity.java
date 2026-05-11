





import java.util.List;
import java.util.ArrayList;

public class typedef_Entity extends Type {

    private int versionuid;





    private List<typedef_Feature> typedef_features;


    public typedef_Entity(
        int versionuid    ) {
        super(
        );
        this.versionuid = versionuid;
        this.typedef_features = new ArrayList<>();
    }

    public typedef_Entity(
        int versionuid        ArrayList<typedef_Feature> typedef_features    ) {
        this.versionuid = versionuid;
        this.typedef_features = typedef_features;
    }

    public int getVersionuid() {
        return versionuid;
    }

    public void setVersionuid(int versionuid) {
        this.versionuid = versionuid;
    }

    public List<typedef_Feature> getTypedef_features() {
        return typedef_features;
    }

    public void addTypedef_feature(Typedef_feature typedef_feature) {
        this.typedef_features.add(typedef_feature);
    }

}