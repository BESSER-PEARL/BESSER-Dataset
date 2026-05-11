





import java.util.List;
import java.util.ArrayList;

public class domainmodel_TypeRef  {

    private boolean multi;





    private domainmodel_Type domainmodel_type;




    private domainmodel_Feature domainmodel_feature;


    public domainmodel_TypeRef(
        boolean multi    ) {
        this.multi = multi;
    }


    public boolean getMulti() {
        return multi;
    }

    public void setMulti(boolean multi) {
        this.multi = multi;
    }

    public domainmodel_Type getDomainmodel_type() {
        return domainmodel_type;
    }

    public void setDomainmodel_type(domainmodel_Type domainmodel_type) {
        this.domainmodel_type = domainmodel_type;
    }
    public domainmodel_Feature getDomainmodel_feature() {
        return domainmodel_feature;
    }

    public void setDomainmodel_feature(domainmodel_Feature domainmodel_feature) {
        this.domainmodel_feature = domainmodel_feature;
    }

}