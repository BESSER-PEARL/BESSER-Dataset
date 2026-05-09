





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_LogicStructure  {

    private String indexCompName;
    private String appComName;





    private softGalleryLanguage_LogicContent softgallerylanguage_logiccontent;


    public softGalleryLanguage_LogicStructure(
        String indexCompName,        String appComName    ) {
        this.indexCompName = indexCompName;
        this.appComName = appComName;
    }


    public String getIndexcompname() {
        return indexCompName;
    }

    public void setIndexcompname(String indexCompName) {
        this.indexCompName = indexCompName;
    }
    public String getAppcomname() {
        return appComName;
    }

    public void setAppcomname(String appComName) {
        this.appComName = appComName;
    }

    public softGalleryLanguage_LogicContent getSoftgallerylanguage_logiccontent() {
        return softgallerylanguage_logiccontent;
    }

    public void setSoftgallerylanguage_logiccontent(softGalleryLanguage_LogicContent softgallerylanguage_logiccontent) {
        this.softgallerylanguage_logiccontent = softgallerylanguage_logiccontent;
    }

}