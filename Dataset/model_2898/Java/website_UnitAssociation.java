





import java.util.List;
import java.util.ArrayList;

public class website_UnitAssociation extends UnitContainer, AssociationReference, UnitFeature {

    private boolean isSourceAssociation;





    private website_EntityOrView website_entityorview;




    private website_Selection website_selection;




    private website_EntityOrView website_entityorview;


    public website_UnitAssociation(
        boolean isSourceAssociation    ) {
        super(
        );
        this.isSourceAssociation = isSourceAssociation;
    }


    public boolean getIssourceassociation() {
        return isSourceAssociation;
    }

    public void setIssourceassociation(boolean isSourceAssociation) {
        this.isSourceAssociation = isSourceAssociation;
    }

    public website_EntityOrView getWebsite_entityorview() {
        return website_entityorview;
    }

    public void setWebsite_entityorview(website_EntityOrView website_entityorview) {
        this.website_entityorview = website_entityorview;
    }
    public website_Selection getWebsite_selection() {
        return website_selection;
    }

    public void setWebsite_selection(website_Selection website_selection) {
        this.website_selection = website_selection;
    }
    public website_EntityOrView getWebsite_entityorview() {
        return website_entityorview;
    }

    public void setWebsite_entityorview(website_EntityOrView website_entityorview) {
        this.website_entityorview = website_entityorview;
    }

}