





import java.util.List;
import java.util.ArrayList;

public class commons_CategoryInfo  {

    private String googleFormalId;
    private String primaryUri;





    private commons_CategoryInfo commons_categoryinfo;


    public commons_CategoryInfo(
        String googleFormalId,        String primaryUri    ) {
        this.googleFormalId = googleFormalId;
        this.primaryUri = primaryUri;
    }


    public String getGoogleformalid() {
        return googleFormalId;
    }

    public void setGoogleformalid(String googleFormalId) {
        this.googleFormalId = googleFormalId;
    }
    public String getPrimaryuri() {
        return primaryUri;
    }

    public void setPrimaryuri(String primaryUri) {
        this.primaryUri = primaryUri;
    }

    public commons_CategoryInfo getCommons_categoryinfo() {
        return commons_categoryinfo;
    }

    public void setCommons_categoryinfo(commons_CategoryInfo commons_categoryinfo) {
        this.commons_categoryinfo = commons_categoryinfo;
    }

}