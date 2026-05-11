





import java.util.List;
import java.util.ArrayList;

public class domainmodel_Entity extends Type {






    private List<domainmodel_Feature> domainmodel_features;




    private domainmodel_Entity domainmodel_entity;


    public domainmodel_Entity(
    ) {
        super(
        );
        this.domainmodel_features = new ArrayList<>();
    }

    public domainmodel_Entity(
        ArrayList<domainmodel_Feature> domainmodel_features    ) {
        this.domainmodel_features = domainmodel_features;
    }


    public List<domainmodel_Feature> getDomainmodel_features() {
        return domainmodel_features;
    }

    public void addDomainmodel_feature(Domainmodel_feature domainmodel_feature) {
        this.domainmodel_features.add(domainmodel_feature);
    }
    public domainmodel_Entity getDomainmodel_entity() {
        return domainmodel_entity;
    }

    public void setDomainmodel_entity(domainmodel_Entity domainmodel_entity) {
        this.domainmodel_entity = domainmodel_entity;
    }

}