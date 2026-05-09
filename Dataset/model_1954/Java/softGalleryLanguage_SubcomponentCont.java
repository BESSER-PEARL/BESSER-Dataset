





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_SubcomponentCont  {

    private String nameSubComp;





    private List<softGalleryLanguage_ComponentClass> softgallerylanguage_componentclasss;




    private softGalleryLanguage_UIContent softgallerylanguage_uicontent;


    public softGalleryLanguage_SubcomponentCont(
        String nameSubComp    ) {
        this.nameSubComp = nameSubComp;
        this.softgallerylanguage_componentclasss = new ArrayList<>();
    }

    public softGalleryLanguage_SubcomponentCont(
        String nameSubComp        ArrayList<softGalleryLanguage_ComponentClass> softgallerylanguage_componentclasss    ) {
        this.nameSubComp = nameSubComp;
        this.softgallerylanguage_componentclasss = softgallerylanguage_componentclasss;
    }

    public String getNamesubcomp() {
        return nameSubComp;
    }

    public void setNamesubcomp(String nameSubComp) {
        this.nameSubComp = nameSubComp;
    }

    public List<softGalleryLanguage_ComponentClass> getSoftgallerylanguage_componentclasss() {
        return softgallerylanguage_componentclasss;
    }

    public void addSoftgallerylanguage_componentclass(Softgallerylanguage_componentclass softgallerylanguage_componentclass) {
        this.softgallerylanguage_componentclasss.add(softgallerylanguage_componentclass);
    }
    public softGalleryLanguage_UIContent getSoftgallerylanguage_uicontent() {
        return softgallerylanguage_uicontent;
    }

    public void setSoftgallerylanguage_uicontent(softGalleryLanguage_UIContent softgallerylanguage_uicontent) {
        this.softgallerylanguage_uicontent = softgallerylanguage_uicontent;
    }

}