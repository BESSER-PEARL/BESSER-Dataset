





import java.util.List;
import java.util.ArrayList;

public class coCoMM_FeatureModel  {

    private boolean isDomain;
    private String id;
    private String name;



    public coCoMM_FeatureModel(
        boolean isDomain,        String id,        String name    ) {
        this.isDomain = isDomain;
        this.id = id;
        this.name = name;
    }


    public boolean getIsdomain() {
        return isDomain;
    }

    public void setIsdomain(boolean isDomain) {
        this.isDomain = isDomain;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}