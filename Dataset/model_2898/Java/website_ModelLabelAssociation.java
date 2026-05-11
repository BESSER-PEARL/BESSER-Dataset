





import java.util.List;
import java.util.ArrayList;

public class website_ModelLabelAssociation extends ModelLabelFeature {

    private boolean isSourceAssociation;





    private website_ModelLabel website_modellabel;


    public website_ModelLabelAssociation(
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

    public website_ModelLabel getWebsite_modellabel() {
        return website_modellabel;
    }

    public void setWebsite_modellabel(website_ModelLabel website_modellabel) {
        this.website_modellabel = website_modellabel;
    }

}