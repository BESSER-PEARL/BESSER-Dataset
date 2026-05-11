





import java.util.List;
import java.util.ArrayList;

public class PhotosMetaModel_Modules  {

    private String name;





    private PhotosMetaModel_React photosmetamodel_react;


    public PhotosMetaModel_Modules(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PhotosMetaModel_React getPhotosmetamodel_react() {
        return photosmetamodel_react;
    }

    public void setPhotosmetamodel_react(PhotosMetaModel_React photosmetamodel_react) {
        this.photosmetamodel_react = photosmetamodel_react;
    }

}