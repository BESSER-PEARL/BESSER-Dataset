





import java.util.List;
import java.util.ArrayList;

public class uma_WorkOrder  {

    private String value;
    private String linkType;
    private String id;
    private String properties;





    private uma_WorkBreakdownElement uma_workbreakdownelement;


    public uma_WorkOrder(
        String value,        String linkType,        String id,        String properties    ) {
        this.value = value;
        this.linkType = linkType;
        this.id = id;
        this.properties = properties;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getLinktype() {
        return linkType;
    }

    public void setLinktype(String linkType) {
        this.linkType = linkType;
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

    public uma_WorkBreakdownElement getUma_workbreakdownelement() {
        return uma_workbreakdownelement;
    }

    public void setUma_workbreakdownelement(uma_WorkBreakdownElement uma_workbreakdownelement) {
        this.uma_workbreakdownelement = uma_workbreakdownelement;
    }

}