





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_StateContent  {

    private String stateName;
    private String componentdatatyp;





    private softGalleryLanguage_State softgallerylanguage_state;


    public softGalleryLanguage_StateContent(
        String stateName,        String componentdatatyp    ) {
        this.stateName = stateName;
        this.componentdatatyp = componentdatatyp;
    }


    public String getStatename() {
        return stateName;
    }

    public void setStatename(String stateName) {
        this.stateName = stateName;
    }
    public String getComponentdatatyp() {
        return componentdatatyp;
    }

    public void setComponentdatatyp(String componentdatatyp) {
        this.componentdatatyp = componentdatatyp;
    }

    public softGalleryLanguage_State getSoftgallerylanguage_state() {
        return softgallerylanguage_state;
    }

    public void setSoftgallerylanguage_state(softGalleryLanguage_State softgallerylanguage_state) {
        this.softgallerylanguage_state = softgallerylanguage_state;
    }

}