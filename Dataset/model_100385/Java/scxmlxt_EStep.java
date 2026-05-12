





import java.util.List;
import java.util.ArrayList;

public class scxmlxt_EStep  {

    private String featureName;





    private scxmlxt_EPath scxmlxt_epath;


    public scxmlxt_EStep(
        String featureName    ) {
        this.featureName = featureName;
    }


    public String getFeaturename() {
        return featureName;
    }

    public void setFeaturename(String featureName) {
        this.featureName = featureName;
    }

    public scxmlxt_EPath getScxmlxt_epath() {
        return scxmlxt_epath;
    }

    public void setScxmlxt_epath(scxmlxt_EPath scxmlxt_epath) {
        this.scxmlxt_epath = scxmlxt_epath;
    }

}