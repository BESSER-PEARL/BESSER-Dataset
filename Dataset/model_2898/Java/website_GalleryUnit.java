





import java.util.List;
import java.util.ArrayList;

public class website_GalleryUnit extends ImageUnit {

    private String contentClass;
    private String styleClass;





    private website_ImageManipulation website_imagemanipulation;


    public website_GalleryUnit(
        String contentClass,        String styleClass    ) {
        super(
        );
        this.contentClass = contentClass;
        this.styleClass = styleClass;
    }


    public String getContentclass() {
        return contentClass;
    }

    public void setContentclass(String contentClass) {
        this.contentClass = contentClass;
    }
    public String getStyleclass() {
        return styleClass;
    }

    public void setStyleclass(String styleClass) {
        this.styleClass = styleClass;
    }

    public website_ImageManipulation getWebsite_imagemanipulation() {
        return website_imagemanipulation;
    }

    public void setWebsite_imagemanipulation(website_ImageManipulation website_imagemanipulation) {
        this.website_imagemanipulation = website_imagemanipulation;
    }

}