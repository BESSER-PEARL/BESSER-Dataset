





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_ResponseParameter  {






    private List<softGalleryLanguage_EObject> softgallerylanguage_eobjects;




    private softGalleryLanguage_ResponseEntity softgallerylanguage_responseentity;


    public softGalleryLanguage_ResponseParameter(
    ) {
        this.softgallerylanguage_eobjects = new ArrayList<>();
    }

    public softGalleryLanguage_ResponseParameter(
        ArrayList<softGalleryLanguage_EObject> softgallerylanguage_eobjects    ) {
        this.softgallerylanguage_eobjects = softgallerylanguage_eobjects;
    }


    public List<softGalleryLanguage_EObject> getSoftgallerylanguage_eobjects() {
        return softgallerylanguage_eobjects;
    }

    public void addSoftgallerylanguage_eobject(Softgallerylanguage_eobject softgallerylanguage_eobject) {
        this.softgallerylanguage_eobjects.add(softgallerylanguage_eobject);
    }
    public softGalleryLanguage_ResponseEntity getSoftgallerylanguage_responseentity() {
        return softgallerylanguage_responseentity;
    }

    public void setSoftgallerylanguage_responseentity(softGalleryLanguage_ResponseEntity softgallerylanguage_responseentity) {
        this.softgallerylanguage_responseentity = softgallerylanguage_responseentity;
    }

}