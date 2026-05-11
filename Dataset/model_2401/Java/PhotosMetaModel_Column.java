





import java.util.List;
import java.util.ArrayList;

public class PhotosMetaModel_Column  {






    private PhotosMetaModel_DataType photosmetamodel_datatype;




    private List<PhotosMetaModel_Constraint> photosmetamodel_constraints;


    public PhotosMetaModel_Column(
    ) {
        this.photosmetamodel_constraints = new ArrayList<>();
    }

    public PhotosMetaModel_Column(
        ArrayList<PhotosMetaModel_Constraint> photosmetamodel_constraints    ) {
        this.photosmetamodel_constraints = photosmetamodel_constraints;
    }


    public PhotosMetaModel_DataType getPhotosmetamodel_datatype() {
        return photosmetamodel_datatype;
    }

    public void setPhotosmetamodel_datatype(PhotosMetaModel_DataType photosmetamodel_datatype) {
        this.photosmetamodel_datatype = photosmetamodel_datatype;
    }
    public List<PhotosMetaModel_Constraint> getPhotosmetamodel_constraints() {
        return photosmetamodel_constraints;
    }

    public void addPhotosmetamodel_constraint(Photosmetamodel_constraint photosmetamodel_constraint) {
        this.photosmetamodel_constraints.add(photosmetamodel_constraint);
    }

}