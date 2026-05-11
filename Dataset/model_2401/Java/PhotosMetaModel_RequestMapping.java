





import java.util.List;
import java.util.ArrayList;

public class PhotosMetaModel_RequestMapping  {






    private PhotosMetaModel_RestController photosmetamodel_restcontroller;




    private List<PhotosMetaModel_RequestPart> photosmetamodel_requestparts;


    public PhotosMetaModel_RequestMapping(
    ) {
        this.photosmetamodel_requestparts = new ArrayList<>();
    }

    public PhotosMetaModel_RequestMapping(
        ArrayList<PhotosMetaModel_RequestPart> photosmetamodel_requestparts    ) {
        this.photosmetamodel_requestparts = photosmetamodel_requestparts;
    }


    public PhotosMetaModel_RestController getPhotosmetamodel_restcontroller() {
        return photosmetamodel_restcontroller;
    }

    public void setPhotosmetamodel_restcontroller(PhotosMetaModel_RestController photosmetamodel_restcontroller) {
        this.photosmetamodel_restcontroller = photosmetamodel_restcontroller;
    }
    public List<PhotosMetaModel_RequestPart> getPhotosmetamodel_requestparts() {
        return photosmetamodel_requestparts;
    }

    public void addPhotosmetamodel_requestpart(Photosmetamodel_requestpart photosmetamodel_requestpart) {
        this.photosmetamodel_requestparts.add(photosmetamodel_requestpart);
    }

}