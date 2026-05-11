





import java.util.List;
import java.util.ArrayList;

public class website_EncapsulatedAssociation extends Association, EncapsulatedFeature {

    private String name;
    private boolean isSourceAssociation;
    private String cardinality;





    private website_ViewAssociation website_viewassociation;




    private website_EncapsulatedAssociation website_encapsulatedassociation;


    public website_EncapsulatedAssociation(
        String name,        boolean isSourceAssociation,        String cardinality    ) {
        super(
        );
        this.name = name;
        this.isSourceAssociation = isSourceAssociation;
        this.cardinality = cardinality;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIssourceassociation() {
        return isSourceAssociation;
    }

    public void setIssourceassociation(boolean isSourceAssociation) {
        this.isSourceAssociation = isSourceAssociation;
    }
    public String getCardinality() {
        return cardinality;
    }

    public void setCardinality(String cardinality) {
        this.cardinality = cardinality;
    }

    public website_ViewAssociation getWebsite_viewassociation() {
        return website_viewassociation;
    }

    public void setWebsite_viewassociation(website_ViewAssociation website_viewassociation) {
        this.website_viewassociation = website_viewassociation;
    }
    public website_EncapsulatedAssociation getWebsite_encapsulatedassociation() {
        return website_encapsulatedassociation;
    }

    public void setWebsite_encapsulatedassociation(website_EncapsulatedAssociation website_encapsulatedassociation) {
        this.website_encapsulatedassociation = website_encapsulatedassociation;
    }

}