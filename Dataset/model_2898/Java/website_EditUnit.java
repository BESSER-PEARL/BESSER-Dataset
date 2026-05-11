





import java.util.List;
import java.util.ArrayList;

public class website_EditUnit extends SingletonUnit, DynamicUnit {

    private String contentClass;
    private boolean customiseValues;
    private String confirmLabel;
    private String cancelLabel;





    private website_Page website_page;




    private website_Predicate website_predicate;




    private website_Page website_page;




    private website_Label website_label;




    private website_Selection website_selection;


    public website_EditUnit(
        String contentClass,        boolean customiseValues,        String confirmLabel,        String cancelLabel    ) {
        super(
        );
        this.contentClass = contentClass;
        this.customiseValues = customiseValues;
        this.confirmLabel = confirmLabel;
        this.cancelLabel = cancelLabel;
    }


    public String getContentclass() {
        return contentClass;
    }

    public void setContentclass(String contentClass) {
        this.contentClass = contentClass;
    }
    public boolean getCustomisevalues() {
        return customiseValues;
    }

    public void setCustomisevalues(boolean customiseValues) {
        this.customiseValues = customiseValues;
    }
    public String getConfirmlabel() {
        return confirmLabel;
    }

    public void setConfirmlabel(String confirmLabel) {
        this.confirmLabel = confirmLabel;
    }
    public String getCancellabel() {
        return cancelLabel;
    }

    public void setCancellabel(String cancelLabel) {
        this.cancelLabel = cancelLabel;
    }

    public website_Page getWebsite_page() {
        return website_page;
    }

    public void setWebsite_page(website_Page website_page) {
        this.website_page = website_page;
    }
    public website_Predicate getWebsite_predicate() {
        return website_predicate;
    }

    public void setWebsite_predicate(website_Predicate website_predicate) {
        this.website_predicate = website_predicate;
    }
    public website_Page getWebsite_page() {
        return website_page;
    }

    public void setWebsite_page(website_Page website_page) {
        this.website_page = website_page;
    }
    public website_Label getWebsite_label() {
        return website_label;
    }

    public void setWebsite_label(website_Label website_label) {
        this.website_label = website_label;
    }
    public website_Selection getWebsite_selection() {
        return website_selection;
    }

    public void setWebsite_selection(website_Selection website_selection) {
        this.website_selection = website_selection;
    }

}