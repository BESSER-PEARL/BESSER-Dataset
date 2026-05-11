





import java.util.List;
import java.util.ArrayList;

public class application_FEEDInterface extends Interface {

    private String allowOrganisationFiltering;
    private String allowPersonFiltering;
    private String allowTypeFiltering;
    private String feedType;
    private String language;
    private String allowMetaTagFiltering;
    private String feedTitle;
    private String allowTagFiltering;
    private String allowCategoryFiltering;



    public application_FEEDInterface(
        String allowOrganisationFiltering,        String allowPersonFiltering,        String allowTypeFiltering,        String feedType,        String language,        String allowMetaTagFiltering,        String feedTitle,        String allowTagFiltering,        String allowCategoryFiltering    ) {
        super(
        );
        this.allowOrganisationFiltering = allowOrganisationFiltering;
        this.allowPersonFiltering = allowPersonFiltering;
        this.allowTypeFiltering = allowTypeFiltering;
        this.feedType = feedType;
        this.language = language;
        this.allowMetaTagFiltering = allowMetaTagFiltering;
        this.feedTitle = feedTitle;
        this.allowTagFiltering = allowTagFiltering;
        this.allowCategoryFiltering = allowCategoryFiltering;
    }


    public String getAlloworganisationfiltering() {
        return allowOrganisationFiltering;
    }

    public void setAlloworganisationfiltering(String allowOrganisationFiltering) {
        this.allowOrganisationFiltering = allowOrganisationFiltering;
    }
    public String getAllowpersonfiltering() {
        return allowPersonFiltering;
    }

    public void setAllowpersonfiltering(String allowPersonFiltering) {
        this.allowPersonFiltering = allowPersonFiltering;
    }
    public String getAllowtypefiltering() {
        return allowTypeFiltering;
    }

    public void setAllowtypefiltering(String allowTypeFiltering) {
        this.allowTypeFiltering = allowTypeFiltering;
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
    public String getFeedtitle() {
        return feedTitle;
    }

    public void setFeedtitle(String feedTitle) {
        this.feedTitle = feedTitle;
    }
    public String getAllowtagfiltering() {
        return allowTagFiltering;
    }

    public void setAllowtagfiltering(String allowTagFiltering) {
        this.allowTagFiltering = allowTagFiltering;
    }
    public String getAllowcategoryfiltering() {
        return allowCategoryFiltering;
    }

    public void setAllowcategoryfiltering(String allowCategoryFiltering) {
        this.allowCategoryFiltering = allowCategoryFiltering;
    }


}