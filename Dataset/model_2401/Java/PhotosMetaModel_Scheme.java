





import java.util.List;
import java.util.ArrayList;

public class PhotosMetaModel_Scheme  {

    private String name;





    private List<PhotosMetaModel_Function_p> photosmetamodel_function_ps;




    private PhotosMetaModel_Database photosmetamodel_database;


    public PhotosMetaModel_Scheme(
        String name    ) {
        this.name = name;
        this.photosmetamodel_function_ps = new ArrayList<>();
    }

    public PhotosMetaModel_Scheme(
        String name        ArrayList<PhotosMetaModel_Function_p> photosmetamodel_function_ps    ) {
        this.name = name;
        this.photosmetamodel_function_ps = photosmetamodel_function_ps;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<PhotosMetaModel_Function_p> getPhotosmetamodel_function_ps() {
        return photosmetamodel_function_ps;
    }

    public void addPhotosmetamodel_function_p(Photosmetamodel_function_p photosmetamodel_function_p) {
        this.photosmetamodel_function_ps.add(photosmetamodel_function_p);
    }
    public PhotosMetaModel_Database getPhotosmetamodel_database() {
        return photosmetamodel_database;
    }

    public void setPhotosmetamodel_database(PhotosMetaModel_Database photosmetamodel_database) {
        this.photosmetamodel_database = photosmetamodel_database;
    }

}