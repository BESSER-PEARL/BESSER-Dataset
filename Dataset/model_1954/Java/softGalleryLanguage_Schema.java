





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_Schema  {






    private List<softGalleryLanguage_EObject> softgallerylanguage_eobjects;




    private softGalleryLanguage_Database softgallerylanguage_database;


    public softGalleryLanguage_Schema(
    ) {
        this.softgallerylanguage_eobjects = new ArrayList<>();
    }

    public softGalleryLanguage_Schema(
        ArrayList<softGalleryLanguage_EObject> softgallerylanguage_eobjects    ) {
        this.softgallerylanguage_eobjects = softgallerylanguage_eobjects;
    }


    public List<softGalleryLanguage_EObject> getSoftgallerylanguage_eobjects() {
        return softgallerylanguage_eobjects;
    }

    public void addSoftgallerylanguage_eobject(Softgallerylanguage_eobject softgallerylanguage_eobject) {
        this.softgallerylanguage_eobjects.add(softgallerylanguage_eobject);
    }
    public softGalleryLanguage_Database getSoftgallerylanguage_database() {
        return softgallerylanguage_database;
    }

    public void setSoftgallerylanguage_database(softGalleryLanguage_Database softgallerylanguage_database) {
        this.softgallerylanguage_database = softgallerylanguage_database;
    }

}