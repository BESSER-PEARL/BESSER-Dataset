





import java.util.List;
import java.util.ArrayList;

public class website_Menu extends NamedDisplayElement {

    private String styleClass;
    private String layoutClass;
    private boolean omitCaption;
    private String captionClass;





    private website_Page website_page;




    private website_WebsiteProperties website_websiteproperties;




    private website_WebGenModel website_webgenmodel;


    public website_Menu(
        String styleClass,        String layoutClass,        boolean omitCaption,        String captionClass    ) {
        super(
        );
        this.styleClass = styleClass;
        this.layoutClass = layoutClass;
        this.omitCaption = omitCaption;
        this.captionClass = captionClass;
    }


    public String getStyleclass() {
        return styleClass;
    }

    public void setStyleclass(String styleClass) {
        this.styleClass = styleClass;
    }
    public String getLayoutclass() {
        return layoutClass;
    }

    public void setLayoutclass(String layoutClass) {
        this.layoutClass = layoutClass;
    }
    public boolean getOmitcaption() {
        return omitCaption;
    }

    public void setOmitcaption(boolean omitCaption) {
        this.omitCaption = omitCaption;
    }
    public String getCaptionclass() {
        return captionClass;
    }

    public void setCaptionclass(String captionClass) {
        this.captionClass = captionClass;
    }

    public website_Page getWebsite_page() {
        return website_page;
    }

    public void setWebsite_page(website_Page website_page) {
        this.website_page = website_page;
    }
    public website_WebsiteProperties getWebsite_websiteproperties() {
        return website_websiteproperties;
    }

    public void setWebsite_websiteproperties(website_WebsiteProperties website_websiteproperties) {
        this.website_websiteproperties = website_websiteproperties;
    }
    public website_WebGenModel getWebsite_webgenmodel() {
        return website_webgenmodel;
    }

    public void setWebsite_webgenmodel(website_WebGenModel website_webgenmodel) {
        this.website_webgenmodel = website_webgenmodel;
    }

}