





import java.util.List;
import java.util.ArrayList;

public class application_OAuthClientScope  {

    private String allowContents;
    private String positiveCategory;
    private String maximumAge;
    private String allowOrganisations;
    private String negativeCategory;
    private String allowPersons;
    private String negativeMetaTag;
    private String positivePerson;
    private String positiveMetaTag;
    private String positiveTag;
    private String positiveOrganisation;
    private String negativeOrganisation;
    private String negativeTag;
    private String identSpecification;
    private String negativePerson;



    public application_OAuthClientScope(
        String allowContents,        String positiveCategory,        String maximumAge,        String allowOrganisations,        String negativeCategory,        String allowPersons,        String negativeMetaTag,        String positivePerson,        String positiveMetaTag,        String positiveTag,        String positiveOrganisation,        String negativeOrganisation,        String negativeTag,        String identSpecification,        String negativePerson    ) {
        this.allowContents = allowContents;
        this.positiveCategory = positiveCategory;
        this.maximumAge = maximumAge;
        this.allowOrganisations = allowOrganisations;
        this.negativeCategory = negativeCategory;
        this.allowPersons = allowPersons;
        this.negativeMetaTag = negativeMetaTag;
        this.positivePerson = positivePerson;
        this.positiveMetaTag = positiveMetaTag;
        this.positiveTag = positiveTag;
        this.positiveOrganisation = positiveOrganisation;
        this.negativeOrganisation = negativeOrganisation;
        this.negativeTag = negativeTag;
        this.identSpecification = identSpecification;
        this.negativePerson = negativePerson;
    }


    public String getAllowcontents() {
        return allowContents;
    }

    public void setAllowcontents(String allowContents) {
        this.allowContents = allowContents;
    }
    public String getPositivecategory() {
        return positiveCategory;
    }

    public void setPositivecategory(String positiveCategory) {
        this.positiveCategory = positiveCategory;
    }
    public String getMaximumage() {
        return maximumAge;
    }

    public void setMaximumage(String maximumAge) {
        this.maximumAge = maximumAge;
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
    public String getPositiveperson() {
        return positivePerson;
    }

    public void setPositiveperson(String positivePerson) {
        this.positivePerson = positivePerson;
    }
    public String getPositivemetatag() {
        return positiveMetaTag;
    }

    public void setPositivemetatag(String positiveMetaTag) {
        this.positiveMetaTag = positiveMetaTag;
    }
    public String getPositivetag() {
        return positiveTag;
    }

    public void setPositivetag(String positiveTag) {
        this.positiveTag = positiveTag;
    }
    public String getPositiveorganisation() {
        return positiveOrganisation;
    }

    public void setPositiveorganisation(String positiveOrganisation) {
        this.positiveOrganisation = positiveOrganisation;
    }
    public String getNegativeorganisation() {
        return negativeOrganisation;
    }

    public void setNegativeorganisation(String negativeOrganisation) {
        this.negativeOrganisation = negativeOrganisation;
    }
    public String getNegativetag() {
        return negativeTag;
    }

    public void setNegativetag(String negativeTag) {
        this.negativeTag = negativeTag;
    }
    public String getIdentspecification() {
        return identSpecification;
    }

    public void setIdentspecification(String identSpecification) {
        this.identSpecification = identSpecification;
    }
    public String getNegativeperson() {
        return negativePerson;
    }

    public void setNegativeperson(String negativePerson) {
        this.negativePerson = negativePerson;
    }


}