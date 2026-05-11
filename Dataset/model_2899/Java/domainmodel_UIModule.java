





import java.util.List;
import java.util.ArrayList;

public class domainmodel_UIModule extends SystemModule {






    private List<domainmodel_UIFeature> domainmodel_uifeatures;


    public domainmodel_UIModule(
    ) {
        super(
        );
        this.domainmodel_uifeatures = new ArrayList<>();
    }

    public domainmodel_UIModule(
        ArrayList<domainmodel_UIFeature> domainmodel_uifeatures    ) {
        this.domainmodel_uifeatures = domainmodel_uifeatures;
    }


    public List<domainmodel_UIFeature> getDomainmodel_uifeatures() {
        return domainmodel_uifeatures;
    }

    public void addDomainmodel_uifeature(Domainmodel_uifeature domainmodel_uifeature) {
        this.domainmodel_uifeatures.add(domainmodel_uifeature);
    }

}