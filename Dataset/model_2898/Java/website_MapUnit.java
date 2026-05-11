





import java.util.List;
import java.util.ArrayList;

public class website_MapUnit extends EditUnit, SelectableUnit {

    private String styleClass;
    private int defaultZoomLevel;
    private boolean readOnly;





    private website_LocationAttribute website_locationattribute;




    private website_Attribute website_attribute;


    public website_MapUnit(
        String styleClass,        int defaultZoomLevel,        boolean readOnly    ) {
        super(
        );
        this.styleClass = styleClass;
        this.defaultZoomLevel = defaultZoomLevel;
        this.readOnly = readOnly;
    }


    public String getStyleclass() {
        return styleClass;
    }

    public void setStyleclass(String styleClass) {
        this.styleClass = styleClass;
    }
    public int getDefaultzoomlevel() {
        return defaultZoomLevel;
    }

    public void setDefaultzoomlevel(int defaultZoomLevel) {
        this.defaultZoomLevel = defaultZoomLevel;
    }
    public boolean getReadonly() {
        return readOnly;
    }

    public void setReadonly(boolean readOnly) {
        this.readOnly = readOnly;
    }

    public website_LocationAttribute getWebsite_locationattribute() {
        return website_locationattribute;
    }

    public void setWebsite_locationattribute(website_LocationAttribute website_locationattribute) {
        this.website_locationattribute = website_locationattribute;
    }
    public website_Attribute getWebsite_attribute() {
        return website_attribute;
    }

    public void setWebsite_attribute(website_Attribute website_attribute) {
        this.website_attribute = website_attribute;
    }

}