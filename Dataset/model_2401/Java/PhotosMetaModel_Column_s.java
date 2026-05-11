





import java.util.List;
import java.util.ArrayList;

public class PhotosMetaModel_Column_s  {

    private String name;





    private PhotosMetaModel_Table_s photosmetamodel_table_s;


    public PhotosMetaModel_Column_s(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PhotosMetaModel_Table_s getPhotosmetamodel_table_s() {
        return photosmetamodel_table_s;
    }

    public void setPhotosmetamodel_table_s(PhotosMetaModel_Table_s photosmetamodel_table_s) {
        this.photosmetamodel_table_s = photosmetamodel_table_s;
    }

}