





import java.util.List;
import java.util.ArrayList;

public class persistence_View extends EntityOrView {






    private persistence_ViewFeature persistence_viewfeature;




    private List<persistence_ViewFeature> persistence_viewfeatures;




    private List<persistence_EntityOrView> persistence_entityorviews;


    public persistence_View(
    ) {
        super(
        );
        this.persistence_viewfeatures = new ArrayList<>();
        this.persistence_entityorviews = new ArrayList<>();
    }

    public persistence_View(
        ArrayList<persistence_ViewFeature> persistence_viewfeatures,        ArrayList<persistence_EntityOrView> persistence_entityorviews    ) {
        this.persistence_viewfeatures = persistence_viewfeatures;
        this.persistence_entityorviews = persistence_entityorviews;
    }


    public persistence_ViewFeature getPersistence_viewfeature() {
        return persistence_viewfeature;
    }

    public void setPersistence_viewfeature(persistence_ViewFeature persistence_viewfeature) {
        this.persistence_viewfeature = persistence_viewfeature;
    }
    public List<persistence_ViewFeature> getPersistence_viewfeatures() {
        return persistence_viewfeatures;
    }

    public void addPersistence_viewfeature(Persistence_viewfeature persistence_viewfeature) {
        this.persistence_viewfeatures.add(persistence_viewfeature);
    }
    public List<persistence_EntityOrView> getPersistence_entityorviews() {
        return persistence_entityorviews;
    }

    public void addPersistence_entityorview(Persistence_entityorview persistence_entityorview) {
        this.persistence_entityorviews.add(persistence_entityorview);
    }

}