





import java.util.List;
import java.util.ArrayList;

public class PhotosMetaModel_State  {

    private String active;





    private PhotosMetaModel_ReactClasses photosmetamodel_reactclasses;


    public PhotosMetaModel_State(
        String active    ) {
        this.active = active;
    }


    public String getActive() {
        return active;
    }

    public void setActive(String active) {
        this.active = active;
    }

    public PhotosMetaModel_ReactClasses getPhotosmetamodel_reactclasses() {
        return photosmetamodel_reactclasses;
    }

    public void setPhotosmetamodel_reactclasses(PhotosMetaModel_ReactClasses photosmetamodel_reactclasses) {
        this.photosmetamodel_reactclasses = photosmetamodel_reactclasses;
    }

}