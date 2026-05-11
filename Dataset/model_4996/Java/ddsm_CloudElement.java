





import java.util.List;
import java.util.ArrayList;

public class ddsm_CloudElement  {

    private String elementId;
    private String description;



    public ddsm_CloudElement(
        String elementId,        String description    ) {
        this.elementId = elementId;
        this.description = description;
    }


    public String getElementid() {
        return elementId;
    }

    public void setElementid(String elementId) {
        this.elementId = elementId;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}