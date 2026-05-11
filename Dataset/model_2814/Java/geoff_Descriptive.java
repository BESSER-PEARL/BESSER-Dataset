





import java.util.List;
import java.util.ArrayList;

public class geoff_Descriptive  {

    private String shortDescription;
    private String longDescription;



    public geoff_Descriptive(
        String shortDescription,        String longDescription    ) {
        this.shortDescription = shortDescription;
        this.longDescription = longDescription;
    }


    public String getShortdescription() {
        return shortDescription;
    }

    public void setShortdescription(String shortDescription) {
        this.shortDescription = shortDescription;
    }
    public String getLongdescription() {
        return longDescription;
    }

    public void setLongdescription(String longDescription) {
        this.longDescription = longDescription;
    }


}