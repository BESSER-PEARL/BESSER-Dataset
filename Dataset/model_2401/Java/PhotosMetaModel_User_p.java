





import java.util.List;
import java.util.ArrayList;

public class PhotosMetaModel_User_p  {

    private String password;
    private String username;





    private List<PhotosMetaModel_Query> photosmetamodel_querys;




    private PhotosMetaModel_Cluster photosmetamodel_cluster;


    public PhotosMetaModel_User_p(
        String password,        String username    ) {
        this.password = password;
        this.username = username;
        this.photosmetamodel_querys = new ArrayList<>();
    }

    public PhotosMetaModel_User_p(
        String password,        String username        ArrayList<PhotosMetaModel_Query> photosmetamodel_querys    ) {
        this.password = password;
        this.username = username;
        this.photosmetamodel_querys = photosmetamodel_querys;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public List<PhotosMetaModel_Query> getPhotosmetamodel_querys() {
        return photosmetamodel_querys;
    }

    public void addPhotosmetamodel_query(Photosmetamodel_query photosmetamodel_query) {
        this.photosmetamodel_querys.add(photosmetamodel_query);
    }
    public PhotosMetaModel_Cluster getPhotosmetamodel_cluster() {
        return photosmetamodel_cluster;
    }

    public void setPhotosmetamodel_cluster(PhotosMetaModel_Cluster photosmetamodel_cluster) {
        this.photosmetamodel_cluster = photosmetamodel_cluster;
    }

}