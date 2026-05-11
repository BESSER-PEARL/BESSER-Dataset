





import java.util.List;
import java.util.ArrayList;

public class domainmodel_InitActionModule extends ControllerElement {






    private List<domainmodel_InitActionFeature> domainmodel_initactionfeatures;


    public domainmodel_InitActionModule(
    ) {
        super(
        );
        this.domainmodel_initactionfeatures = new ArrayList<>();
    }

    public domainmodel_InitActionModule(
        ArrayList<domainmodel_InitActionFeature> domainmodel_initactionfeatures    ) {
        this.domainmodel_initactionfeatures = domainmodel_initactionfeatures;
    }


    public List<domainmodel_InitActionFeature> getDomainmodel_initactionfeatures() {
        return domainmodel_initactionfeatures;
    }

    public void addDomainmodel_initactionfeature(Domainmodel_initactionfeature domainmodel_initactionfeature) {
        this.domainmodel_initactionfeatures.add(domainmodel_initactionfeature);
    }

}