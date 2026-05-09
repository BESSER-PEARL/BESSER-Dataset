





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_Cluster  {






    private List<softGalleryLanguage_EObject> softgallerylanguage_eobjects;




    private softGalleryLanguage_PostgreSQL softgallerylanguage_postgresql;


    public softGalleryLanguage_Cluster(
    ) {
        this.softgallerylanguage_eobjects = new ArrayList<>();
    }

    public softGalleryLanguage_Cluster(
        ArrayList<softGalleryLanguage_EObject> softgallerylanguage_eobjects    ) {
        this.softgallerylanguage_eobjects = softgallerylanguage_eobjects;
    }


    public List<softGalleryLanguage_EObject> getSoftgallerylanguage_eobjects() {
        return softgallerylanguage_eobjects;
    }

    public void addSoftgallerylanguage_eobject(Softgallerylanguage_eobject softgallerylanguage_eobject) {
        this.softgallerylanguage_eobjects.add(softgallerylanguage_eobject);
    }
    public softGalleryLanguage_PostgreSQL getSoftgallerylanguage_postgresql() {
        return softgallerylanguage_postgresql;
    }

    public void setSoftgallerylanguage_postgresql(softGalleryLanguage_PostgreSQL softgallerylanguage_postgresql) {
        this.softgallerylanguage_postgresql = softgallerylanguage_postgresql;
    }

}