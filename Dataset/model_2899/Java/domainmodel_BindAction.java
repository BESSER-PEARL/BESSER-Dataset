





import java.util.List;
import java.util.ArrayList;

public class domainmodel_BindAction extends InitActionFeature {

    private String attribute;





    private domainmodel_BindSource domainmodel_bindsource;


    public domainmodel_BindAction(
        String attribute    ) {
        super(
        );
        this.attribute = attribute;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }

    public domainmodel_BindSource getDomainmodel_bindsource() {
        return domainmodel_bindsource;
    }

    public void setDomainmodel_bindsource(domainmodel_BindSource domainmodel_bindsource) {
        this.domainmodel_bindsource = domainmodel_bindsource;
    }

}