





import java.util.List;
import java.util.ArrayList;

public class website_FeatureSupportAction extends InlineAction {

    private String fileExtension;
    private String uriElement;
    private String confirmMessage;





    private website_BusinessOperation website_businessoperation;


    public website_FeatureSupportAction(
        String fileExtension,        String uriElement,        String confirmMessage    ) {
        super(
        );
        this.fileExtension = fileExtension;
        this.uriElement = uriElement;
        this.confirmMessage = confirmMessage;
    }


    public String getFileextension() {
        return fileExtension;
    }

    public void setFileextension(String fileExtension) {
        this.fileExtension = fileExtension;
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

    public website_BusinessOperation getWebsite_businessoperation() {
        return website_businessoperation;
    }

    public void setWebsite_businessoperation(website_BusinessOperation website_businessoperation) {
        this.website_businessoperation = website_businessoperation;
    }

}