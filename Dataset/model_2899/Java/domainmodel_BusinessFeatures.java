





import java.util.List;
import java.util.ArrayList;

public class domainmodel_BusinessFeatures extends BusinessModule {






    private List<domainmodel_BusinessFeature> domainmodel_businessfeatures;


    public domainmodel_BusinessFeatures(
    ) {
        super(
        );
        this.domainmodel_businessfeatures = new ArrayList<>();
    }

    public domainmodel_BusinessFeatures(
        ArrayList<domainmodel_BusinessFeature> domainmodel_businessfeatures    ) {
        this.domainmodel_businessfeatures = domainmodel_businessfeatures;
    }


    public List<domainmodel_BusinessFeature> getDomainmodel_businessfeatures() {
        return domainmodel_businessfeatures;
    }

    public void addDomainmodel_businessfeature(Domainmodel_businessfeature domainmodel_businessfeature) {
        this.domainmodel_businessfeatures.add(domainmodel_businessfeature);
    }

}