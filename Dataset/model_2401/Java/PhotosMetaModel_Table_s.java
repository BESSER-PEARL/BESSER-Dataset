





import java.util.List;
import java.util.ArrayList;

public class PhotosMetaModel_Table_s  {

    private String name;





    private PhotosMetaModel_Entity photosmetamodel_entity;


    public PhotosMetaModel_Table_s(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PhotosMetaModel_Entity getPhotosmetamodel_entity() {
        return photosmetamodel_entity;
    }

    public void setPhotosmetamodel_entity(PhotosMetaModel_Entity photosmetamodel_entity) {
        this.photosmetamodel_entity = photosmetamodel_entity;
    }

}