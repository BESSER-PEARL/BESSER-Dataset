





import java.util.List;
import java.util.ArrayList;

public class uma_WorkOrder  {

    private String id;
    private String properties;
    private String linkType;
    private String value;





    private uma_WorkBreakdownElement uma_workbreakdownelement;


    public uma_WorkOrder(
        String id,        String properties,        String linkType,        String value    ) {
        this.id = id;
        this.properties = properties;
        this.linkType = linkType;
        this.value = value;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getProperties() {
        return properties;
    }

    public void setProperties(String properties) {
        this.properties = properties;
    }
    public String getLinktype() {
        return linkType;
    }

    public void setLinktype(String linkType) {
        this.linkType = linkType;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public uma_WorkBreakdownElement getUma_workbreakdownelement() {
        return uma_workbreakdownelement;
    }

    public void setUma_workbreakdownelement(uma_WorkBreakdownElement uma_workbreakdownelement) {
        this.uma_workbreakdownelement = uma_workbreakdownelement;
    }

}