





import java.util.List;
import java.util.ArrayList;

public class PhotosMetaModel_Files  {

    private String extension;
    private String type;





    private PhotosMetaModel_Directories photosmetamodel_directories;




    private PhotosMetaModel_SegmentStructure photosmetamodel_segmentstructure;


    public PhotosMetaModel_Files(
        String extension,        String type    ) {
        this.extension = extension;
        this.type = type;
    }


    public String getExtension() {
        return extension;
    }

    public void setExtension(String extension) {
        this.extension = extension;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public PhotosMetaModel_Directories getPhotosmetamodel_directories() {
        return photosmetamodel_directories;
    }

    public void setPhotosmetamodel_directories(PhotosMetaModel_Directories photosmetamodel_directories) {
        this.photosmetamodel_directories = photosmetamodel_directories;
    }
    public PhotosMetaModel_SegmentStructure getPhotosmetamodel_segmentstructure() {
        return photosmetamodel_segmentstructure;
    }

    public void setPhotosmetamodel_segmentstructure(PhotosMetaModel_SegmentStructure photosmetamodel_segmentstructure) {
        this.photosmetamodel_segmentstructure = photosmetamodel_segmentstructure;
    }

}