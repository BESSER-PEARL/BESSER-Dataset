





import java.util.List;
import java.util.ArrayList;

public class PhotosMetaModel_Folder_a  {

    private String name;





    private List<PhotosMetaModel_File_a> photosmetamodel_file_as;


    public PhotosMetaModel_Folder_a(
        String name    ) {
        this.name = name;
        this.photosmetamodel_file_as = new ArrayList<>();
    }

    public PhotosMetaModel_Folder_a(
        String name        ArrayList<PhotosMetaModel_File_a> photosmetamodel_file_as    ) {
        this.name = name;
        this.photosmetamodel_file_as = photosmetamodel_file_as;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<PhotosMetaModel_File_a> getPhotosmetamodel_file_as() {
        return photosmetamodel_file_as;
    }

    public void addPhotosmetamodel_file_a(Photosmetamodel_file_a photosmetamodel_file_a) {
        this.photosmetamodel_file_as.add(photosmetamodel_file_a);
    }

}