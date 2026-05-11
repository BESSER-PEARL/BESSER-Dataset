





import java.util.List;
import java.util.ArrayList;

public class PhotosMetaModel_Cluster  {






    private List<PhotosMetaModel_Database> photosmetamodel_databases;




    private PhotosMetaModel_PostgreSQL photosmetamodel_postgresql;


    public PhotosMetaModel_Cluster(
    ) {
        this.photosmetamodel_databases = new ArrayList<>();
    }

    public PhotosMetaModel_Cluster(
        ArrayList<PhotosMetaModel_Database> photosmetamodel_databases    ) {
        this.photosmetamodel_databases = photosmetamodel_databases;
    }


    public List<PhotosMetaModel_Database> getPhotosmetamodel_databases() {
        return photosmetamodel_databases;
    }

    public void addPhotosmetamodel_database(Photosmetamodel_database photosmetamodel_database) {
        this.photosmetamodel_databases.add(photosmetamodel_database);
    }
    public PhotosMetaModel_PostgreSQL getPhotosmetamodel_postgresql() {
        return photosmetamodel_postgresql;
    }

    public void setPhotosmetamodel_postgresql(PhotosMetaModel_PostgreSQL photosmetamodel_postgresql) {
        this.photosmetamodel_postgresql = photosmetamodel_postgresql;
    }

}