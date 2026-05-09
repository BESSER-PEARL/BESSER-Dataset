





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_PropsType  {

    private String propsdatas;
    private String nameProps;





    private softGalleryLanguage_Props softgallerylanguage_props;


    public softGalleryLanguage_PropsType(
        String propsdatas,        String nameProps    ) {
        this.propsdatas = propsdatas;
        this.nameProps = nameProps;
    }


    public String getPropsdatas() {
        return propsdatas;
    }

    public void setPropsdatas(String propsdatas) {
        this.propsdatas = propsdatas;
    }
    public String getNameprops() {
        return nameProps;
    }

    public void setNameprops(String nameProps) {
        this.nameProps = nameProps;
    }

    public softGalleryLanguage_Props getSoftgallerylanguage_props() {
        return softgallerylanguage_props;
    }

    public void setSoftgallerylanguage_props(softGalleryLanguage_Props softgallerylanguage_props) {
        this.softgallerylanguage_props = softgallerylanguage_props;
    }

}