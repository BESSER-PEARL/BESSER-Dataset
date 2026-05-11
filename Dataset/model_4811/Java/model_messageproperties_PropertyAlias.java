





import java.util.List;
import java.util.ArrayList;

public class model_messageproperties_PropertyAlias extends ExtensibilityElement {

    private String messageType;
    private String propertyName;
    private String ID;
    private String type;
    private String XSDElement;
    private String part;





    private Part part;


    public model_messageproperties_PropertyAlias(
        String messageType,        String propertyName,        String ID,        String type,        String XSDElement,        String part    ) {
        super(
        );
        this.messageType = messageType;
        this.propertyName = propertyName;
        this.ID = ID;
        this.type = type;
        this.XSDElement = XSDElement;
        this.part = part;
    }


    public String getMessagetype() {
        return messageType;
    }

    public void setMessagetype(String messageType) {
        this.messageType = messageType;
    }
    public String getPropertyname() {
        return propertyName;
    }

    public void setPropertyname(String propertyName) {
        this.propertyName = propertyName;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getXsdelement() {
        return XSDElement;
    }

    public void setXsdelement(String XSDElement) {
        this.XSDElement = XSDElement;
    }
    public String getPart() {
        return part;
    }

    public void setPart(String part) {
        this.part = part;
    }

    public Part getPart() {
        return part;
    }

    public void setPart(Part part) {
        this.part = part;
    }

}