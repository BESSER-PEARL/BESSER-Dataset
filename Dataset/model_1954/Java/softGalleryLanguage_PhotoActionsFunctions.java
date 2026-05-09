





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_PhotoActionsFunctions  {

    private String namePhoto;
    private String nameLoad;
    private String nameGenerico;





    private softGalleryLanguage_PhotoActions softgallerylanguage_photoactions;


    public softGalleryLanguage_PhotoActionsFunctions(
        String namePhoto,        String nameLoad,        String nameGenerico    ) {
        this.namePhoto = namePhoto;
        this.nameLoad = nameLoad;
        this.nameGenerico = nameGenerico;
    }


    public String getNamephoto() {
        return namePhoto;
    }

    public void setNamephoto(String namePhoto) {
        this.namePhoto = namePhoto;
    }
    public String getNameload() {
        return nameLoad;
    }

    public void setNameload(String nameLoad) {
        this.nameLoad = nameLoad;
    }
    public String getNamegenerico() {
        return nameGenerico;
    }

    public void setNamegenerico(String nameGenerico) {
        this.nameGenerico = nameGenerico;
    }

    public softGalleryLanguage_PhotoActions getSoftgallerylanguage_photoactions() {
        return softgallerylanguage_photoactions;
    }

    public void setSoftgallerylanguage_photoactions(softGalleryLanguage_PhotoActions softgallerylanguage_photoactions) {
        this.softgallerylanguage_photoactions = softgallerylanguage_photoactions;
    }

}