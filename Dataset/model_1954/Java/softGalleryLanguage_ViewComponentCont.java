





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_ViewComponentCont  {

    private String nameView;





    private List<softGalleryLanguage_ComponentClass> softgallerylanguage_componentclasss;




    private softGalleryLanguage_UIContent softgallerylanguage_uicontent;


    public softGalleryLanguage_ViewComponentCont(
        String nameView    ) {
        this.nameView = nameView;
        this.softgallerylanguage_componentclasss = new ArrayList<>();
    }

    public softGalleryLanguage_ViewComponentCont(
        String nameView        ArrayList<softGalleryLanguage_ComponentClass> softgallerylanguage_componentclasss    ) {
        this.nameView = nameView;
        this.softgallerylanguage_componentclasss = softgallerylanguage_componentclasss;
    }

    public String getNameview() {
        return nameView;
    }

    public void setNameview(String nameView) {
        this.nameView = nameView;
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