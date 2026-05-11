





import java.util.List;
import java.util.ArrayList;

public class application_OAuthClientScope  {

    private String negativePerson;
    private String negativeOrganisation;
    private String negativeMetaTag;
    private String positiveCategory;
    private String positiveOrganisation;
    private String positiveTag;
    private String identSpecification;
    private String allowOrganisations;
    private String negativeCategory;
    private String positiveMetaTag;
    private String maximumAge;
    private String negativeTag;
    private String allowContents;
    private String allowPersons;
    private String positivePerson;





    private application_OAuthClientConfig application_oauthclientconfig;


    public application_OAuthClientScope(
        String negativePerson,        String negativeOrganisation,        String negativeMetaTag,        String positiveCategory,        String positiveOrganisation,        String positiveTag,        String identSpecification,        String allowOrganisations,        String negativeCategory,        String positiveMetaTag,        String maximumAge,        String negativeTag,        String allowContents,        String allowPersons,        String positivePerson    ) {
        this.negativePerson = negativePerson;
        this.negativeOrganisation = negativeOrganisation;
        this.negativeMetaTag = negativeMetaTag;
        this.positiveCategory = positiveCategory;
        this.positiveOrganisation = positiveOrganisation;
        this.positiveTag = positiveTag;
        this.identSpecification = identSpecification;
        this.allowOrganisations = allowOrganisations;
        this.negativeCategory = negativeCategory;
        this.positiveMetaTag = positiveMetaTag;
        this.maximumAge = maximumAge;
        this.negativeTag = negativeTag;
        this.allowContents = allowContents;
        this.allowPersons = allowPersons;
        this.positivePerson = positivePerson;
    }


    public String getNegativeperson() {
        return negativePerson;
    }

    public void setNegativeperson(String negativePerson) {
        this.negativePerson = negativePerson;
    }
    public String getNegativeorganisation() {
        return negativeOrganisation;
    }

    public void setNegativeorganisation(String negativeOrganisation) {
        this.negativeOrganisation = negativeOrganisation;
    }
    public String getNegativemetatag() {
        return negativeMetaTag;
    }

    public void setNegativemetatag(String negativeMetaTag) {
        this.negativeMetaTag = negativeMetaTag;
    }
    public String getPositivecategory() {
        return positiveCategory;
    }

    public void setPositivecategory(String positiveCategory) {
        this.positiveCategory = positiveCategory;
    }
    public String getPositiveorganisation() {
        return positiveOrganisation;
    }

    public void setPositiveorganisation(String positiveOrganisation) {
        this.positiveOrganisation = positiveOrganisation;
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
    public String getAlloworganisations() {
        return allowOrganisations;
    }

    public void setAlloworganisations(String allowOrganisations) {
        this.allowOrganisations = allowOrganisations;
    }
    public String getNegativecategory() {
        return negativeCategory;
    }

    public void setNegativecategory(String negativeCategory) {
        this.negativeCategory = negativeCategory;
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
    public String getNegativetag() {
        return negativeTag;
    }

    public void setNegativetag(String negativeTag) {
        this.negativeTag = negativeTag;
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
    public String getPositiveperson() {
        return positivePerson;
    }

    public void setPositiveperson(String positivePerson) {
        this.positivePerson = positivePerson;
    }

    public application_OAuthClientConfig getApplication_oauthclientconfig() {
        return application_oauthclientconfig;
    }

    public void setApplication_oauthclientconfig(application_OAuthClientConfig application_oauthclientconfig) {
        this.application_oauthclientconfig = application_oauthclientconfig;
    }

}