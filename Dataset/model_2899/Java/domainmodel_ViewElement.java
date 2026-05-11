





import java.util.List;
import java.util.ArrayList;

public class domainmodel_ViewElement  {

    private String name;





    private domainmodel_ContainerElement domainmodel_containerelement;




    private domainmodel_ViewModule domainmodel_viewmodule;


    public domainmodel_ViewElement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public domainmodel_ContainerElement getDomainmodel_containerelement() {
        return domainmodel_containerelement;
    }

    public void setDomainmodel_containerelement(domainmodel_ContainerElement domainmodel_containerelement) {
        this.domainmodel_containerelement = domainmodel_containerelement;
    }
    public domainmodel_ViewModule getDomainmodel_viewmodule() {
        return domainmodel_viewmodule;
    }

    public void setDomainmodel_viewmodule(domainmodel_ViewModule domainmodel_viewmodule) {
        this.domainmodel_viewmodule = domainmodel_viewmodule;
    }

}