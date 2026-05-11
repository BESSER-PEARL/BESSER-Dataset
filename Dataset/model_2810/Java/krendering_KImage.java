





import java.util.List;
import java.util.ArrayList;

public class krendering_KImage extends KContainerRendering {

    private String imagePath;
    private String bundleName;
    private String imageObject;



    public krendering_KImage(
        String imagePath,        String bundleName,        String imageObject    ) {
        super(
        );
        this.imagePath = imagePath;
        this.bundleName = bundleName;
        this.imageObject = imageObject;
    }


    public String getImagepath() {
        return imagePath;
    }

    public void setImagepath(String imagePath) {
        this.imagePath = imagePath;
    }
    public String getBundlename() {
        return bundleName;
    }

    public void setBundlename(String bundleName) {
        this.bundleName = bundleName;
    }
    public String getImageobject() {
        return imageObject;
    }

    public void setImageobject(String imageObject) {
        this.imageObject = imageObject;
    }


}