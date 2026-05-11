





import java.util.List;
import java.util.ArrayList;

public class website_Authentication  {

    private String loginLabel;
    private String logoutLabel;





    private website_WebsiteProperties website_websiteproperties;




    private website_EntityOrView website_entityorview;




    private website_WebsiteProperties website_websiteproperties;


    public website_Authentication(
        String loginLabel,        String logoutLabel    ) {
        this.loginLabel = loginLabel;
        this.logoutLabel = logoutLabel;
    }


    public String getLoginlabel() {
        return loginLabel;
    }

    public void setLoginlabel(String loginLabel) {
        this.loginLabel = loginLabel;
    }
    public String getLogoutlabel() {
        return logoutLabel;
    }

    public void setLogoutlabel(String logoutLabel) {
        this.logoutLabel = logoutLabel;
    }

    public website_WebsiteProperties getWebsite_websiteproperties() {
        return website_websiteproperties;
    }

    public void setWebsite_websiteproperties(website_WebsiteProperties website_websiteproperties) {
        this.website_websiteproperties = website_websiteproperties;
    }
    public website_EntityOrView getWebsite_entityorview() {
        return website_entityorview;
    }

    public void setWebsite_entityorview(website_EntityOrView website_entityorview) {
        this.website_entityorview = website_entityorview;
    }
    public website_WebsiteProperties getWebsite_websiteproperties() {
        return website_websiteproperties;
    }

    public void setWebsite_websiteproperties(website_WebsiteProperties website_websiteproperties) {
        this.website_websiteproperties = website_websiteproperties;
    }

}