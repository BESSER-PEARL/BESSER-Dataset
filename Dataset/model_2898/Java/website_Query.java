





import java.util.List;
import java.util.ArrayList;

public class website_Query  {






    private website_ActionMenuEntry website_actionmenuentry;




    private List<website_QueryParameter> website_queryparameters;




    private website_Filter website_filter;


    public website_Query(
    ) {
        this.website_queryparameters = new ArrayList<>();
    }

    public website_Query(
        ArrayList<website_QueryParameter> website_queryparameters    ) {
        this.website_queryparameters = website_queryparameters;
    }


    public website_ActionMenuEntry getWebsite_actionmenuentry() {
        return website_actionmenuentry;
    }

    public void setWebsite_actionmenuentry(website_ActionMenuEntry website_actionmenuentry) {
        this.website_actionmenuentry = website_actionmenuentry;
    }
    public List<website_QueryParameter> getWebsite_queryparameters() {
        return website_queryparameters;
    }

    public void addWebsite_queryparameter(Website_queryparameter website_queryparameter) {
        this.website_queryparameters.add(website_queryparameter);
    }
    public website_Filter getWebsite_filter() {
        return website_filter;
    }

    public void setWebsite_filter(website_Filter website_filter) {
        this.website_filter = website_filter;
    }

}