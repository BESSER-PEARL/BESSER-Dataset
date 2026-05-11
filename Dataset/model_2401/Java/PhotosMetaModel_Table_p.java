





import java.util.List;
import java.util.ArrayList;

public class PhotosMetaModel_Table_p  {

    private String name;





    private List<PhotosMetaModel_Row> photosmetamodel_rows;




    private PhotosMetaModel_Scheme photosmetamodel_scheme;




    private PhotosMetaModel_Table_p photosmetamodel_table_p;




    private List<PhotosMetaModel_Column_p> photosmetamodel_column_ps;




    private List<PhotosMetaModel_Column_p> photosmetamodel_column_ps;




    private List<PhotosMetaModel_ForeignKey> photosmetamodel_foreignkeys;




    private PhotosMetaModel_ForeignKey photosmetamodel_foreignkey;


    public PhotosMetaModel_Table_p(
        String name    ) {
        this.name = name;
        this.photosmetamodel_rows = new ArrayList<>();
        this.photosmetamodel_column_ps = new ArrayList<>();
        this.photosmetamodel_column_ps = new ArrayList<>();
        this.photosmetamodel_foreignkeys = new ArrayList<>();
    }

    public PhotosMetaModel_Table_p(
        String name        ArrayList<PhotosMetaModel_Row> photosmetamodel_rows,        ArrayList<PhotosMetaModel_Column_p> photosmetamodel_column_ps,        ArrayList<PhotosMetaModel_Column_p> photosmetamodel_column_ps,        ArrayList<PhotosMetaModel_ForeignKey> photosmetamodel_foreignkeys    ) {
        this.name = name;
        this.photosmetamodel_rows = photosmetamodel_rows;
        this.photosmetamodel_column_ps = photosmetamodel_column_ps;
        this.photosmetamodel_column_ps = photosmetamodel_column_ps;
        this.photosmetamodel_foreignkeys = photosmetamodel_foreignkeys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<PhotosMetaModel_Row> getPhotosmetamodel_rows() {
        return photosmetamodel_rows;
    }

    public void addPhotosmetamodel_row(Photosmetamodel_row photosmetamodel_row) {
        this.photosmetamodel_rows.add(photosmetamodel_row);
    }
    public PhotosMetaModel_Scheme getPhotosmetamodel_scheme() {
        return photosmetamodel_scheme;
    }

    public void setPhotosmetamodel_scheme(PhotosMetaModel_Scheme photosmetamodel_scheme) {
        this.photosmetamodel_scheme = photosmetamodel_scheme;
    }
    public PhotosMetaModel_Table_p getPhotosmetamodel_table_p() {
        return photosmetamodel_table_p;
    }

    public void setPhotosmetamodel_table_p(PhotosMetaModel_Table_p photosmetamodel_table_p) {
        this.photosmetamodel_table_p = photosmetamodel_table_p;
    }
    public List<PhotosMetaModel_Column_p> getPhotosmetamodel_column_ps() {
        return photosmetamodel_column_ps;
    }

    public void addPhotosmetamodel_column_p(Photosmetamodel_column_p photosmetamodel_column_p) {
        this.photosmetamodel_column_ps.add(photosmetamodel_column_p);
    }
    public List<PhotosMetaModel_Column_p> getPhotosmetamodel_column_ps() {
        return photosmetamodel_column_ps;
    }

    public void addPhotosmetamodel_column_p(Photosmetamodel_column_p photosmetamodel_column_p) {
        this.photosmetamodel_column_ps.add(photosmetamodel_column_p);
    }
    public List<PhotosMetaModel_ForeignKey> getPhotosmetamodel_foreignkeys() {
        return photosmetamodel_foreignkeys;
    }

    public void addPhotosmetamodel_foreignkey(Photosmetamodel_foreignkey photosmetamodel_foreignkey) {
        this.photosmetamodel_foreignkeys.add(photosmetamodel_foreignkey);
    }
    public PhotosMetaModel_ForeignKey getPhotosmetamodel_foreignkey() {
        return photosmetamodel_foreignkey;
    }

    public void setPhotosmetamodel_foreignkey(PhotosMetaModel_ForeignKey photosmetamodel_foreignkey) {
        this.photosmetamodel_foreignkey = photosmetamodel_foreignkey;
    }

}