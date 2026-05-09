





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_NTiersRelations  {

    private String name;





    private softGalleryLanguage_NTierSource softgallerylanguage_ntiersource;




    private softGalleryLanguage_NTierTarget softgallerylanguage_ntiertarget;


    public softGalleryLanguage_NTiersRelations(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public softGalleryLanguage_NTierSource getSoftgallerylanguage_ntiersource() {
        return softgallerylanguage_ntiersource;
    }

    public void setSoftgallerylanguage_ntiersource(softGalleryLanguage_NTierSource softgallerylanguage_ntiersource) {
        this.softgallerylanguage_ntiersource = softgallerylanguage_ntiersource;
    }
    public softGalleryLanguage_NTierTarget getSoftgallerylanguage_ntiertarget() {
        return softgallerylanguage_ntiertarget;
    }

    public void setSoftgallerylanguage_ntiertarget(softGalleryLanguage_NTierTarget softgallerylanguage_ntiertarget) {
        this.softgallerylanguage_ntiertarget = softgallerylanguage_ntiertarget;
    }

}