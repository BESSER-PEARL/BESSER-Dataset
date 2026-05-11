





import java.util.List;
import java.util.ArrayList;

public class PhotosMetaModel_BusinessLogic extends Layer {






    private List<PhotosMetaModel_BusinessLogicSegment> photosmetamodel_businesslogicsegments;


    public PhotosMetaModel_BusinessLogic(
    ) {
        super(
        );
        this.photosmetamodel_businesslogicsegments = new ArrayList<>();
    }

    public PhotosMetaModel_BusinessLogic(
        ArrayList<PhotosMetaModel_BusinessLogicSegment> photosmetamodel_businesslogicsegments    ) {
        this.photosmetamodel_businesslogicsegments = photosmetamodel_businesslogicsegments;
    }


    public List<PhotosMetaModel_BusinessLogicSegment> getPhotosmetamodel_businesslogicsegments() {
        return photosmetamodel_businesslogicsegments;
    }

    public void addPhotosmetamodel_businesslogicsegment(Photosmetamodel_businesslogicsegment photosmetamodel_businesslogicsegment) {
        this.photosmetamodel_businesslogicsegments.add(photosmetamodel_businesslogicsegment);
    }

}