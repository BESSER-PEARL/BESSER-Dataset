





import java.util.List;
import java.util.ArrayList;

public class website_FeatureReference extends Path {

    private String name;





    private website_Feature website_feature;


    public website_FeatureReference(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public website_Feature getWebsite_feature() {
        return website_feature;
    }

    public void setWebsite_feature(website_Feature website_feature) {
        this.website_feature = website_feature;
    }

}