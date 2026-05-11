





import java.util.List;
import java.util.ArrayList;

public class application_FEEDInterface extends Interface {

    private String allowOrganisationFiltering;
    private String feedType;
    private String language;
    private String allowTagFiltering;
    private String allowTypeFiltering;
    private String feedTitle;
    private String allowPersonFiltering;
    private String allowCategoryFiltering;
    private String allowMetaTagFiltering;



    public application_FEEDInterface(
        String allowOrganisationFiltering,        String feedType,        String language,        String allowTagFiltering,        String allowTypeFiltering,        String feedTitle,        String allowPersonFiltering,        String allowCategoryFiltering,        String allowMetaTagFiltering    ) {
        super(
        );
        this.allowOrganisationFiltering = allowOrganisationFiltering;
        this.feedType = feedType;
        this.language = language;
        this.allowTagFiltering = allowTagFiltering;
        this.allowTypeFiltering = allowTypeFiltering;
        this.feedTitle = feedTitle;
        this.allowPersonFiltering = allowPersonFiltering;
        this.allowCategoryFiltering = allowCategoryFiltering;
        this.allowMetaTagFiltering = allowMetaTagFiltering;
    }


    public String getAlloworganisationfiltering() {
        return allowOrganisationFiltering;
    }

    public void setAlloworganisationfiltering(String allowOrganisationFiltering) {
        this.allowOrganisationFiltering = allowOrganisationFiltering;
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
    public String getAllowtagfiltering() {
        return allowTagFiltering;
    }

    public void setAllowtagfiltering(String allowTagFiltering) {
        this.allowTagFiltering = allowTagFiltering;
    }
    public String getAllowtypefiltering() {
        return allowTypeFiltering;
    }

    public void setAllowtypefiltering(String allowTypeFiltering) {
        this.allowTypeFiltering = allowTypeFiltering;
    }
    public String getFeedtitle() {
        return feedTitle;
    }

    public void setFeedtitle(String feedTitle) {
        this.feedTitle = feedTitle;
    }
    public String getAllowpersonfiltering() {
        return allowPersonFiltering;
    }

    public void setAllowpersonfiltering(String allowPersonFiltering) {
        this.allowPersonFiltering = allowPersonFiltering;
    }
    public String getAllowcategoryfiltering() {
        return allowCategoryFiltering;
    }

    public void setAllowcategoryfiltering(String allowCategoryFiltering) {
        this.allowCategoryFiltering = allowCategoryFiltering;
    }
    public String getAllowmetatagfiltering() {
        return allowMetaTagFiltering;
    }

    public void setAllowmetatagfiltering(String allowMetaTagFiltering) {
        this.allowMetaTagFiltering = allowMetaTagFiltering;
    }


}