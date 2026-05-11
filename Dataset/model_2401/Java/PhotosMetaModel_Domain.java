





import java.util.List;
import java.util.ArrayList;

public class PhotosMetaModel_Domain  {






    private List<PhotosMetaModel_Entities> photosmetamodel_entitiess;




    private PhotosMetaModel_SoftGallery photosmetamodel_softgallery;




    private List<PhotosMetaModel_Functionalities> photosmetamodel_functionalitiess;


    public PhotosMetaModel_Domain(
    ) {
        this.photosmetamodel_entitiess = new ArrayList<>();
        this.photosmetamodel_functionalitiess = new ArrayList<>();
    }

    public PhotosMetaModel_Domain(
        ArrayList<PhotosMetaModel_Entities> photosmetamodel_entitiess,        ArrayList<PhotosMetaModel_Functionalities> photosmetamodel_functionalitiess    ) {
        this.photosmetamodel_entitiess = photosmetamodel_entitiess;
        this.photosmetamodel_functionalitiess = photosmetamodel_functionalitiess;
    }


    public List<PhotosMetaModel_Entities> getPhotosmetamodel_entitiess() {
        return photosmetamodel_entitiess;
    }

    public void addPhotosmetamodel_entities(Photosmetamodel_entities photosmetamodel_entities) {
        this.photosmetamodel_entitiess.add(photosmetamodel_entities);
    }
    public PhotosMetaModel_SoftGallery getPhotosmetamodel_softgallery() {
        return photosmetamodel_softgallery;
    }

    public void setPhotosmetamodel_softgallery(PhotosMetaModel_SoftGallery photosmetamodel_softgallery) {
        this.photosmetamodel_softgallery = photosmetamodel_softgallery;
    }
    public List<PhotosMetaModel_Functionalities> getPhotosmetamodel_functionalitiess() {
        return photosmetamodel_functionalitiess;
    }

    public void addPhotosmetamodel_functionalities(Photosmetamodel_functionalities photosmetamodel_functionalities) {
        this.photosmetamodel_functionalitiess.add(photosmetamodel_functionalities);
    }

}