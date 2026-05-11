





import java.util.List;
import java.util.ArrayList;

public class coCoMM_FeatureModel  {

    private String name;
    private boolean isDomain;



    public coCoMM_FeatureModel(
        String name,        boolean isDomain    ) {
        this.name = name;
        this.isDomain = isDomain;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsdomain() {
        return isDomain;
    }

    public void setIsdomain(boolean isDomain) {
        this.isDomain = isDomain;
    }


}