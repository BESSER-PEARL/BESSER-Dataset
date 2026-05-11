





import java.util.List;
import java.util.ArrayList;

public class website_Filter extends NamedDisplayElement {






    private website_FilterParameter website_filterparameter;




    private website_Selection website_selection;




    private List<website_FilterParameter> website_filterparameters;


    public website_Filter(
    ) {
        super(
        );
        this.website_filterparameters = new ArrayList<>();
    }

    public website_Filter(
        ArrayList<website_FilterParameter> website_filterparameters    ) {
        this.website_filterparameters = website_filterparameters;
    }


    public website_FilterParameter getWebsite_filterparameter() {
        return website_filterparameter;
    }

    public void setWebsite_filterparameter(website_FilterParameter website_filterparameter) {
        this.website_filterparameter = website_filterparameter;
    }
    public website_Selection getWebsite_selection() {
        return website_selection;
    }

    public void setWebsite_selection(website_Selection website_selection) {
        this.website_selection = website_selection;
    }
    public List<website_FilterParameter> getWebsite_filterparameters() {
        return website_filterparameters;
    }

    public void addWebsite_filterparameter(Website_filterparameter website_filterparameter) {
        this.website_filterparameters.add(website_filterparameter);
    }

}