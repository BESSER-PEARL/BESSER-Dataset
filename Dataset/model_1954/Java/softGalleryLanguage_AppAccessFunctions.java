





import java.util.List;
import java.util.ArrayList;

public class softGalleryLanguage_AppAccessFunctions  {

    private String loginName;
    private String registerName;





    private softGalleryLanguage_AppAccess softgallerylanguage_appaccess;


    public softGalleryLanguage_AppAccessFunctions(
        String loginName,        String registerName    ) {
        this.loginName = loginName;
        this.registerName = registerName;
    }


    public String getLoginname() {
        return loginName;
    }

    public void setLoginname(String loginName) {
        this.loginName = loginName;
    }
    public String getRegistername() {
        return registerName;
    }

    public void setRegistername(String registerName) {
        this.registerName = registerName;
    }

    public softGalleryLanguage_AppAccess getSoftgallerylanguage_appaccess() {
        return softgallerylanguage_appaccess;
    }

    public void setSoftgallerylanguage_appaccess(softGalleryLanguage_AppAccess softgallerylanguage_appaccess) {
        this.softgallerylanguage_appaccess = softgallerylanguage_appaccess;
    }

}