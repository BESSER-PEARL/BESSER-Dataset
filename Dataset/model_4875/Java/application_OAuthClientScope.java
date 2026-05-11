





import java.util.List;
import java.util.ArrayList;

public class application_OAuthClientScope  {

    private String allowPersons;
    private String identSpecification;
    private String negativeTag;
    private String positiveTag;
    private String negativeCategory;
    private String positiveOrganisation;
    private String negativeOrganisation;
    private String negativeMetaTag;
    private String positiveMetaTag;
    private String positivePerson;
    private String allowContents;
    private String allowOrganisations;
    private String negativePerson;
    private String maximumAge;
    private String positiveCategory;



    public application_OAuthClientScope(
        String allowPersons,        String identSpecification,        String negativeTag,        String positiveTag,        String negativeCategory,        String positiveOrganisation,        String negativeOrganisation,        String negativeMetaTag,        String positiveMetaTag,        String positivePerson,        String allowContents,        String allowOrganisations,        String negativePerson,        String maximumAge,        String positiveCategory    ) {
        this.allowPersons = allowPersons;
        this.identSpecification = identSpecification;
        this.negativeTag = negativeTag;
        this.positiveTag = positiveTag;
        this.negativeCategory = negativeCategory;
        this.positiveOrganisation = positiveOrganisation;
        this.negativeOrganisation = negativeOrganisation;
        this.negativeMetaTag = negativeMetaTag;
        this.positiveMetaTag = positiveMetaTag;
        this.positivePerson = positivePerson;
        this.allowContents = allowContents;
        this.allowOrganisations = allowOrganisations;
        this.negativePerson = negativePerson;
        this.maximumAge = maximumAge;
        this.positiveCategory = positiveCategory;
    }


    public String getAllowpersons() {
        return allowPersons;
    }

    public void setAllowpersons(String allowPersons) {
        this.allowPersons = allowPersons;
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
    public String getPositivetag() {
        return positiveTag;
    }

    public void setPositivetag(String positiveTag) {
        this.positiveTag = positiveTag;
    }
    public String getNegativecategory() {
        return negativeCategory;
    }

    public void setNegativecategory(String negativeCategory) {
        this.negativeCategory = negativeCategory;
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
    public String getNegativemetatag() {
        return negativeMetaTag;
    }

    public void setNegativemetatag(String negativeMetaTag) {
        this.negativeMetaTag = negativeMetaTag;
    }
    public String getPositivemetatag() {
        return positiveMetaTag;
    }

    public void setPositivemetatag(String positiveMetaTag) {
        this.positiveMetaTag = positiveMetaTag;
    }
    public String getPositiveperson() {
        return positivePerson;
    }

    public void setPositiveperson(String positivePerson) {
        this.positivePerson = positivePerson;
    }
    public String getAllowcontents() {
        return allowContents;
    }

    public void setAllowcontents(String allowContents) {
        this.allowContents = allowContents;
    }
    public String getAlloworganisations() {
        return allowOrganisations;
    }

    public void setAlloworganisations(String allowOrganisations) {
        this.allowOrganisations = allowOrganisations;
    }
    public String getNegativeperson() {
        return negativePerson;
    }

    public void setNegativeperson(String negativePerson) {
        this.negativePerson = negativePerson;
    }
    public String getMaximumage() {
        return maximumAge;
    }

    public void setMaximumage(String maximumAge) {
        this.maximumAge = maximumAge;
    }
    public String getPositivecategory() {
        return positiveCategory;
    }

    public void setPositivecategory(String positiveCategory) {
        this.positiveCategory = positiveCategory;
    }


}