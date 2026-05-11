





import java.util.List;
import java.util.ArrayList;

public class website_CreateSitemapUnit extends ContentUnit {

    private String contentClass;
    private String filename;
    private String styleClass;
    private String deployedURL;



    public website_CreateSitemapUnit(
        String contentClass,        String filename,        String styleClass,        String deployedURL    ) {
        super(
        );
        this.contentClass = contentClass;
        this.filename = filename;
        this.styleClass = styleClass;
        this.deployedURL = deployedURL;
    }


    public String getContentclass() {
        return contentClass;
    }

    public void setContentclass(String contentClass) {
        this.contentClass = contentClass;
    }
    public String getFilename() {
        return filename;
    }

    public void setFilename(String filename) {
        this.filename = filename;
    }
    public String getStyleclass() {
        return styleClass;
    }

    public void setStyleclass(String styleClass) {
        this.styleClass = styleClass;
    }
    public String getDeployedurl() {
        return deployedURL;
    }

    public void setDeployedurl(String deployedURL) {
        this.deployedURL = deployedURL;
    }


}