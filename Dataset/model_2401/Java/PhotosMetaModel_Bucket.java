





import java.util.List;
import java.util.ArrayList;

public class PhotosMetaModel_Bucket  {

    private String name;





    private PhotosMetaModel_AmazonSimpleStorageService photosmetamodel_amazonsimplestorageservice;




    private List<PhotosMetaModel_Folder_a> photosmetamodel_folder_as;




    private List<PhotosMetaModel_File_a> photosmetamodel_file_as;




    private PhotosMetaModel_Access photosmetamodel_access;


    public PhotosMetaModel_Bucket(
        String name    ) {
        this.name = name;
        this.photosmetamodel_folder_as = new ArrayList<>();
        this.photosmetamodel_file_as = new ArrayList<>();
    }

    public PhotosMetaModel_Bucket(
        String name        ArrayList<PhotosMetaModel_Folder_a> photosmetamodel_folder_as,        ArrayList<PhotosMetaModel_File_a> photosmetamodel_file_as    ) {
        this.name = name;
        this.photosmetamodel_folder_as = photosmetamodel_folder_as;
        this.photosmetamodel_file_as = photosmetamodel_file_as;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PhotosMetaModel_AmazonSimpleStorageService getPhotosmetamodel_amazonsimplestorageservice() {
        return photosmetamodel_amazonsimplestorageservice;
    }

    public void setPhotosmetamodel_amazonsimplestorageservice(PhotosMetaModel_AmazonSimpleStorageService photosmetamodel_amazonsimplestorageservice) {
        this.photosmetamodel_amazonsimplestorageservice = photosmetamodel_amazonsimplestorageservice;
    }
    public List<PhotosMetaModel_Folder_a> getPhotosmetamodel_folder_as() {
        return photosmetamodel_folder_as;
    }

    public void addPhotosmetamodel_folder_a(Photosmetamodel_folder_a photosmetamodel_folder_a) {
        this.photosmetamodel_folder_as.add(photosmetamodel_folder_a);
    }
    public List<PhotosMetaModel_File_a> getPhotosmetamodel_file_as() {
        return photosmetamodel_file_as;
    }

    public void addPhotosmetamodel_file_a(Photosmetamodel_file_a photosmetamodel_file_a) {
        this.photosmetamodel_file_as.add(photosmetamodel_file_a);
    }
    public PhotosMetaModel_Access getPhotosmetamodel_access() {
        return photosmetamodel_access;
    }

    public void setPhotosmetamodel_access(PhotosMetaModel_Access photosmetamodel_access) {
        this.photosmetamodel_access = photosmetamodel_access;
    }

}