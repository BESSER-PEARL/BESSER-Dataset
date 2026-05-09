





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_ReactsRelationServ  {

    private String name;





    private List<softGalleryLanguage_ReactServicesType> softgallerylanguage_reactservicestypes;




    private softGalleryLanguage_ReactServicesRelation softgallerylanguage_reactservicesrelation;


    public softGalleryLanguage_ReactsRelationServ(
        String name    ) {
        this.name = name;
        this.softgallerylanguage_reactservicestypes = new ArrayList<>();
    }

    public softGalleryLanguage_ReactsRelationServ(
        String name        ArrayList<softGalleryLanguage_ReactServicesType> softgallerylanguage_reactservicestypes    ) {
        this.name = name;
        this.softgallerylanguage_reactservicestypes = softgallerylanguage_reactservicestypes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<softGalleryLanguage_ReactServicesType> getSoftgallerylanguage_reactservicestypes() {
        return softgallerylanguage_reactservicestypes;
    }

    public void addSoftgallerylanguage_reactservicestype(Softgallerylanguage_reactservicestype softgallerylanguage_reactservicestype) {
        this.softgallerylanguage_reactservicestypes.add(softgallerylanguage_reactservicestype);
    }
    public softGalleryLanguage_ReactServicesRelation getSoftgallerylanguage_reactservicesrelation() {
        return softgallerylanguage_reactservicesrelation;
    }

    public void setSoftgallerylanguage_reactservicesrelation(softGalleryLanguage_ReactServicesRelation softgallerylanguage_reactservicesrelation) {
        this.softgallerylanguage_reactservicesrelation = softgallerylanguage_reactservicesrelation;
    }

}