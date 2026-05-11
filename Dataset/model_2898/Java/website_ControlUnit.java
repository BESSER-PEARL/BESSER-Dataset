





import java.util.List;
import java.util.ArrayList;

public class website_ControlUnit extends DynamicUnit {

    private String contentClass;
    private String cancelLabel;
    private String submitLabel;





    private website_Page website_page;


    public website_ControlUnit(
        String contentClass,        String cancelLabel,        String submitLabel    ) {
        super(
        );
        this.contentClass = contentClass;
        this.cancelLabel = cancelLabel;
        this.submitLabel = submitLabel;
    }


    public String getContentclass() {
        return contentClass;
    }

    public void setContentclass(String contentClass) {
        this.contentClass = contentClass;
    }
    public String getCancellabel() {
        return cancelLabel;
    }

    public void setCancellabel(String cancelLabel) {
        this.cancelLabel = cancelLabel;
    }
    public String getSubmitlabel() {
        return submitLabel;
    }

    public void setSubmitlabel(String submitLabel) {
        this.submitLabel = submitLabel;
    }

    public website_Page getWebsite_page() {
        return website_page;
    }

    public void setWebsite_page(website_Page website_page) {
        this.website_page = website_page;
    }

}