





import java.util.List;
import java.util.ArrayList;

public class PhotosMetaModel_Column_p  {

    private String name;





    private List<PhotosMetaModel_Constraint> photosmetamodel_constraints;




    private PhotosMetaModel_DataType photosmetamodel_datatype;


    public PhotosMetaModel_Column_p(
        String name    ) {
        this.name = name;
        this.photosmetamodel_constraints = new ArrayList<>();
    }

    public PhotosMetaModel_Column_p(
        String name        ArrayList<PhotosMetaModel_Constraint> photosmetamodel_constraints    ) {
        this.name = name;
        this.photosmetamodel_constraints = photosmetamodel_constraints;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<PhotosMetaModel_Constraint> getPhotosmetamodel_constraints() {
        return photosmetamodel_constraints;
    }

    public void addPhotosmetamodel_constraint(Photosmetamodel_constraint photosmetamodel_constraint) {
        this.photosmetamodel_constraints.add(photosmetamodel_constraint);
    }
    public PhotosMetaModel_DataType getPhotosmetamodel_datatype() {
        return photosmetamodel_datatype;
    }

    public void setPhotosmetamodel_datatype(PhotosMetaModel_DataType photosmetamodel_datatype) {
        this.photosmetamodel_datatype = photosmetamodel_datatype;
    }

}