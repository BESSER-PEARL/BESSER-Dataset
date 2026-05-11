





import java.util.List;
import java.util.ArrayList;

public class PhotosMetaModel_Props  {

    private String type;
    private String dataType;





    private PhotosMetaModel_ReactClasses photosmetamodel_reactclasses;


    public PhotosMetaModel_Props(
        String type,        String dataType    ) {
        this.type = type;
        this.dataType = dataType;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }

    public PhotosMetaModel_ReactClasses getPhotosmetamodel_reactclasses() {
        return photosmetamodel_reactclasses;
    }

    public void setPhotosmetamodel_reactclasses(PhotosMetaModel_ReactClasses photosmetamodel_reactclasses) {
        this.photosmetamodel_reactclasses = photosmetamodel_reactclasses;
    }

}