





import java.util.List;
import java.util.ArrayList;

public class website_QueryParameter  {

    private String value;





    private website_FilterParameter website_filterparameter;


    public website_QueryParameter(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public website_FilterParameter getWebsite_filterparameter() {
        return website_filterparameter;
    }

    public void setWebsite_filterparameter(website_FilterParameter website_filterparameter) {
        this.website_filterparameter = website_filterparameter;
    }

}