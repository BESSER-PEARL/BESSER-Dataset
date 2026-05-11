





import java.util.List;
import java.util.ArrayList;

public class website_View extends EntityOrView {






    private website_ViewFeature website_viewfeature;




    private List<website_ViewFeature> website_viewfeatures;




    private List<website_EntityOrView> website_entityorviews;


    public website_View(
    ) {
        super(
        );
        this.website_viewfeatures = new ArrayList<>();
        this.website_entityorviews = new ArrayList<>();
    }

    public website_View(
        ArrayList<website_ViewFeature> website_viewfeatures,        ArrayList<website_EntityOrView> website_entityorviews    ) {
        this.website_viewfeatures = website_viewfeatures;
        this.website_entityorviews = website_entityorviews;
    }


    public website_ViewFeature getWebsite_viewfeature() {
        return website_viewfeature;
    }

    public void setWebsite_viewfeature(website_ViewFeature website_viewfeature) {
        this.website_viewfeature = website_viewfeature;
    }
    public List<website_ViewFeature> getWebsite_viewfeatures() {
        return website_viewfeatures;
    }

    public void addWebsite_viewfeature(Website_viewfeature website_viewfeature) {
        this.website_viewfeatures.add(website_viewfeature);
    }
    public List<website_EntityOrView> getWebsite_entityorviews() {
        return website_entityorviews;
    }

    public void addWebsite_entityorview(Website_entityorview website_entityorview) {
        this.website_entityorviews.add(website_entityorview);
    }

}