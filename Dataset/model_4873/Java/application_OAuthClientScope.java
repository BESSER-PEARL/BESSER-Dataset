





import java.util.List;
import java.util.ArrayList;

public class application_OAuthClientScope  {

    private String positiveOrganisation;
    private String positivePerson;
    private String negativeCategory;
    private String negativeOrganisation;
    private String allowOrganisations;
    private String positiveTag;
    private String identSpecification;
    private String negativeTag;
    private String negativePerson;
    private String positiveCategory;
    private String positiveMetaTag;
    private String maximumAge;
    private String allowContents;
    private String allowPersons;
    private String negativeMetaTag;





    private application_OAuthClientConfig application_oauthclientconfig;


    public application_OAuthClientScope(
        String positiveOrganisation,        String positivePerson,        String negativeCategory,        String negativeOrganisation,        String allowOrganisations,        String positiveTag,        String identSpecification,        String negativeTag,        String negativePerson,        String positiveCategory,        String positiveMetaTag,        String maximumAge,        String allowContents,        String allowPersons,        String negativeMetaTag    ) {
        this.positiveOrganisation = positiveOrganisation;
        this.positivePerson = positivePerson;
        this.negativeCategory = negativeCategory;
        this.negativeOrganisation = negativeOrganisation;
        this.allowOrganisations = allowOrganisations;
        this.positiveTag = positiveTag;
        this.identSpecification = identSpecification;
        this.negativeTag = negativeTag;
        this.negativePerson = negativePerson;
        this.positiveCategory = positiveCategory;
        this.positiveMetaTag = positiveMetaTag;
        this.maximumAge = maximumAge;
        this.allowContents = allowContents;
        this.allowPersons = allowPersons;
        this.negativeMetaTag = negativeMetaTag;
    }


    public String getPositiveorganisation() {
        return positiveOrganisation;
    }

    public void setPositiveorganisation(String positiveOrganisation) {
        this.positiveOrganisation = positiveOrganisation;
    }
    public String getPositiveperson() {
        return positivePerson;
    }

    public void setPositiveperson(String positivePerson) {
        this.positivePerson = positivePerson;
    }
    public String getNegativecategory() {
        return negativeCategory;
    }

    public void setNegativecategory(String negativeCategory) {
        this.negativeCategory = negativeCategory;
    }
    public String getNegativeorganisation() {
        return negativeOrganisation;
    }

    public void setNegativeorganisation(String negativeOrganisation) {
        this.negativeOrganisation = negativeOrganisation;
    }
    public String getAlloworganisations() {
        return allowOrganisations;
    }

    public void setAlloworganisations(String allowOrganisations) {
        this.allowOrganisations = allowOrganisations;
    }
    public String getPositivetag() {
        return positiveTag;
    }

    public void setPositivetag(String positiveTag) {
        this.positiveTag = positiveTag;
    }
    public String getIdentspecification() {
        return identSpecification;
    }

    public void setIdentspecification(String identSpecification) {
        this.identSpecification = identSpecification;
    }
    public String getNegativetag() {
        return negativeTag;
    }

    public void setNegativetag(String negativeTag) {
        this.negativeTag = negativeTag;
    }
    public String getNegativeperson() {
        return negativePerson;
    }

    public void setNegativeperson(String negativePerson) {
        this.negativePerson = negativePerson;
    }
    public String getPositivecategory() {
        return positiveCategory;
    }

    public void setPositivecategory(String positiveCategory) {
        this.positiveCategory = positiveCategory;
    }
    public String getPositivemetatag() {
        return positiveMetaTag;
    }

    public void setPositivemetatag(String positiveMetaTag) {
        this.positiveMetaTag = positiveMetaTag;
    }
    public String getMaximumage() {
        return maximumAge;
    }

    public void setMaximumage(String maximumAge) {
        this.maximumAge = maximumAge;
    }
    public String getAllowcontents() {
        return allowContents;
    }

    public void setAllowcontents(String allowContents) {
        this.allowContents = allowContents;
    }
    public String getAllowpersons() {
        return allowPersons;
    }

    public void setAllowpersons(String allowPersons) {
        this.allowPersons = allowPersons;
    }
    public String getNegativemetatag() {
        return negativeMetaTag;
    }

    public void setNegativemetatag(String negativeMetaTag) {
        this.negativeMetaTag = negativeMetaTag;
    }

    public application_OAuthClientConfig getApplication_oauthclientconfig() {
        return application_oauthclientconfig;
    }

    public void setApplication_oauthclientconfig(application_OAuthClientConfig application_oauthclientconfig) {
        this.application_oauthclientconfig = application_oauthclientconfig;
    }

}