





import java.util.List;
import java.util.ArrayList;

public class website_UnitContainer  {






    private website_ContentUnit website_contentunit;




    private List<website_ContentUnit> website_contentunits;


    public website_UnitContainer(
    ) {
        this.website_contentunits = new ArrayList<>();
    }

    public website_UnitContainer(
        ArrayList<website_ContentUnit> website_contentunits    ) {
        this.website_contentunits = website_contentunits;
    }


    public website_ContentUnit getWebsite_contentunit() {
        return website_contentunit;
    }

    public void setWebsite_contentunit(website_ContentUnit website_contentunit) {
        this.website_contentunit = website_contentunit;
    }
    public List<website_ContentUnit> getWebsite_contentunits() {
        return website_contentunits;
    }

    public void addWebsite_contentunit(Website_contentunit website_contentunit) {
        this.website_contentunits.add(website_contentunit);
    }

}