





import java.util.List;
import java.util.ArrayList;

public class application_FEEDInterface extends Interface {

    private String allowPersonFiltering;
    private String feedTitle;
    private String allowTypeFiltering;
    private String allowOrganisationFiltering;
    private String allowCategoryFiltering;
    private String allowTagFiltering;
    private String feedType;
    private String language;
    private String allowMetaTagFiltering;



    public application_FEEDInterface(
        String allowPersonFiltering,        String feedTitle,        String allowTypeFiltering,        String allowOrganisationFiltering,        String allowCategoryFiltering,        String allowTagFiltering,        String feedType,        String language,        String allowMetaTagFiltering    ) {
        super(
        );
        this.allowPersonFiltering = allowPersonFiltering;
        this.feedTitle = feedTitle;
        this.allowTypeFiltering = allowTypeFiltering;
        this.allowOrganisationFiltering = allowOrganisationFiltering;
        this.allowCategoryFiltering = allowCategoryFiltering;
        this.allowTagFiltering = allowTagFiltering;
        this.feedType = feedType;
        this.language = language;
        this.allowMetaTagFiltering = allowMetaTagFiltering;
    }


    public String getAllowpersonfiltering() {
        return allowPersonFiltering;
    }

    public void setAllowpersonfiltering(String allowPersonFiltering) {
        this.allowPersonFiltering = allowPersonFiltering;
    }
    public String getFeedtitle() {
        return feedTitle;
    }

    public void setFeedtitle(String feedTitle) {
        this.feedTitle = feedTitle;
    }
    public String getAllowtypefiltering() {
        return allowTypeFiltering;
    }

    public void setAllowtypefiltering(String allowTypeFiltering) {
        this.allowTypeFiltering = allowTypeFiltering;
    }
    public String getAlloworganisationfiltering() {
        return allowOrganisationFiltering;
    }

    public void setAlloworganisationfiltering(String allowOrganisationFiltering) {
        this.allowOrganisationFiltering = allowOrganisationFiltering;
    }
    public String getAllowcategoryfiltering() {
        return allowCategoryFiltering;
    }

    public void setAllowcategoryfiltering(String allowCategoryFiltering) {
        this.allowCategoryFiltering = allowCategoryFiltering;
    }
    public String getAllowtagfiltering() {
        return allowTagFiltering;
    }

    public void setAllowtagfiltering(String allowTagFiltering) {
        this.allowTagFiltering = allowTagFiltering;
    }
    public String getFeedtype() {
        return feedType;
    }

    public void setFeedtype(String feedType) {
        this.feedType = feedType;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getAllowmetatagfiltering() {
        return allowMetaTagFiltering;
    }

    public void setAllowmetatagfiltering(String allowMetaTagFiltering) {
        this.allowMetaTagFiltering = allowMetaTagFiltering;
    }


}