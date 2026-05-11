





import java.util.List;
import java.util.ArrayList;

public class domainmodel_Type extends AbstractElement {

    private String name;





    private domainmodel_Feature domainmodel_feature;


    public domainmodel_Type(
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

    public domainmodel_Feature getDomainmodel_feature() {
        return domainmodel_feature;
    }

    public void setDomainmodel_feature(domainmodel_Feature domainmodel_feature) {
        this.domainmodel_feature = domainmodel_feature;
    }

}