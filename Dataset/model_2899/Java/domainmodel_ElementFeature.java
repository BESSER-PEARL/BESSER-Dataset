





import java.util.List;
import java.util.ArrayList;

public class domainmodel_ElementFeature  {

    private String propertyName;
    private String propertyValue;





    private domainmodel_ViewElement domainmodel_viewelement;


    public domainmodel_ElementFeature(
        String propertyName,        String propertyValue    ) {
        this.propertyName = propertyName;
        this.propertyValue = propertyValue;
    }


    public String getPropertyname() {
        return propertyName;
    }

    public void setPropertyname(String propertyName) {
        this.propertyName = propertyName;
    }
    public String getPropertyvalue() {
        return propertyValue;
    }

    public void setPropertyvalue(String propertyValue) {
        this.propertyValue = propertyValue;
    }

    public domainmodel_ViewElement getDomainmodel_viewelement() {
        return domainmodel_viewelement;
    }

    public void setDomainmodel_viewelement(domainmodel_ViewElement domainmodel_viewelement) {
        this.domainmodel_viewelement = domainmodel_viewelement;
    }

}