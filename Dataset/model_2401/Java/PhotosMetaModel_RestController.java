





import java.util.List;
import java.util.ArrayList;

public class PhotosMetaModel_RestController  {

    private String name;





    private PhotosMetaModel_SpringBootApplication photosmetamodel_springbootapplication;


    public PhotosMetaModel_RestController(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PhotosMetaModel_SpringBootApplication getPhotosmetamodel_springbootapplication() {
        return photosmetamodel_springbootapplication;
    }

    public void setPhotosmetamodel_springbootapplication(PhotosMetaModel_SpringBootApplication photosmetamodel_springbootapplication) {
        this.photosmetamodel_springbootapplication = photosmetamodel_springbootapplication;
    }

}