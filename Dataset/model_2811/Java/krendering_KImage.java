





import java.util.List;
import java.util.ArrayList;

public class krendering_KImage extends KContainerRendering {

    private String bundleName;
    private String imagePath;
    private String imageObject;





    private krendering_KRendering krendering_krendering;


    public krendering_KImage(
        String bundleName,        String imagePath,        String imageObject    ) {
        super(
        );
        this.bundleName = bundleName;
        this.imagePath = imagePath;
        this.imageObject = imageObject;
    }


    public String getBundlename() {
        return bundleName;
    }

    public void setBundlename(String bundleName) {
        this.bundleName = bundleName;
    }
    public String getImagepath() {
        return imagePath;
    }

    public void setImagepath(String imagePath) {
        this.imagePath = imagePath;
    }
    public String getImageobject() {
        return imageObject;
    }

    public void setImageobject(String imageObject) {
        this.imageObject = imageObject;
    }

    public krendering_KRendering getKrendering_krendering() {
        return krendering_krendering;
    }

    public void setKrendering_krendering(krendering_KRendering krendering_krendering) {
        this.krendering_krendering = krendering_krendering;
    }

}