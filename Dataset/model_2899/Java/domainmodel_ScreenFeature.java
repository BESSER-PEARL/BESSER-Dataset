





import java.util.List;
import java.util.ArrayList;

public class domainmodel_ScreenFeature extends UIFeature {

    private String name;





    private domainmodel_NavigateToAction domainmodel_navigatetoaction;


    public domainmodel_ScreenFeature(
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

    public domainmodel_NavigateToAction getDomainmodel_navigatetoaction() {
        return domainmodel_navigatetoaction;
    }

    public void setDomainmodel_navigatetoaction(domainmodel_NavigateToAction domainmodel_navigatetoaction) {
        this.domainmodel_navigatetoaction = domainmodel_navigatetoaction;
    }

}