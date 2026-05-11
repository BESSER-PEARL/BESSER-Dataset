





import java.util.List;
import java.util.ArrayList;

public class website_DeleteAction extends InlineAction {

    private String uriElement;
    private String confirmMessage;





    private website_Page website_page;


    public website_DeleteAction(
        String uriElement,        String confirmMessage    ) {
        super(
        );
        this.uriElement = uriElement;
        this.confirmMessage = confirmMessage;
    }


    public String getUrielement() {
        return uriElement;
    }

    public void setUrielement(String uriElement) {
        this.uriElement = uriElement;
    }
    public String getConfirmmessage() {
        return confirmMessage;
    }

    public void setConfirmmessage(String confirmMessage) {
        this.confirmMessage = confirmMessage;
    }

    public website_Page getWebsite_page() {
        return website_page;
    }

    public void setWebsite_page(website_Page website_page) {
        this.website_page = website_page;
    }

}