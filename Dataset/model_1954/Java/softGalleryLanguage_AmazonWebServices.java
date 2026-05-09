





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_AmazonWebServices  {

    private String name;





    private softGalleryLanguage_Technologies softgallerylanguage_technologies;




    private List<softGalleryLanguage_EObject> softgallerylanguage_eobjects;


    public softGalleryLanguage_AmazonWebServices(
        String name    ) {
        this.name = name;
        this.softgallerylanguage_eobjects = new ArrayList<>();
    }

    public softGalleryLanguage_AmazonWebServices(
        String name        ArrayList<softGalleryLanguage_EObject> softgallerylanguage_eobjects    ) {
        this.name = name;
        this.softgallerylanguage_eobjects = softgallerylanguage_eobjects;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public softGalleryLanguage_Technologies getSoftgallerylanguage_technologies() {
        return softgallerylanguage_technologies;
    }

    public void setSoftgallerylanguage_technologies(softGalleryLanguage_Technologies softgallerylanguage_technologies) {
        this.softgallerylanguage_technologies = softgallerylanguage_technologies;
    }
    public List<softGalleryLanguage_EObject> getSoftgallerylanguage_eobjects() {
        return softgallerylanguage_eobjects;
    }

    public void addSoftgallerylanguage_eobject(Softgallerylanguage_eobject softgallerylanguage_eobject) {
        this.softgallerylanguage_eobjects.add(softgallerylanguage_eobject);
    }

}