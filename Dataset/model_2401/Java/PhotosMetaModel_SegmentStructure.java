





import java.util.List;
import java.util.ArrayList;

public class PhotosMetaModel_SegmentStructure  {

    private String name;





    private PhotosMetaModel_DataSegment photosmetamodel_datasegment;




    private PhotosMetaModel_BusinessLogicSegment photosmetamodel_businesslogicsegment;


    public PhotosMetaModel_SegmentStructure(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PhotosMetaModel_DataSegment getPhotosmetamodel_datasegment() {
        return photosmetamodel_datasegment;
    }

    public void setPhotosmetamodel_datasegment(PhotosMetaModel_DataSegment photosmetamodel_datasegment) {
        this.photosmetamodel_datasegment = photosmetamodel_datasegment;
    }
    public PhotosMetaModel_BusinessLogicSegment getPhotosmetamodel_businesslogicsegment() {
        return photosmetamodel_businesslogicsegment;
    }

    public void setPhotosmetamodel_businesslogicsegment(PhotosMetaModel_BusinessLogicSegment photosmetamodel_businesslogicsegment) {
        this.photosmetamodel_businesslogicsegment = photosmetamodel_businesslogicsegment;
    }

}