





import java.util.List;
import java.util.ArrayList;

public class ddsm_Property  {

    private String value;
    private String propertyId;





    private ddsm_CloudElement ddsm_cloudelement;


    public ddsm_Property(
        String value,        String propertyId    ) {
        this.value = value;
        this.propertyId = propertyId;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getPropertyid() {
        return propertyId;
    }

    public void setPropertyid(String propertyId) {
        this.propertyId = propertyId;
    }

    public ddsm_CloudElement getDdsm_cloudelement() {
        return ddsm_cloudelement;
    }

    public void setDdsm_cloudelement(ddsm_CloudElement ddsm_cloudelement) {
        this.ddsm_cloudelement = ddsm_cloudelement;
    }

}