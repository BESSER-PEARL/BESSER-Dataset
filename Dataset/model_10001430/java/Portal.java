





import java.util.List;
import java.util.ArrayList;

public class Portal  {

    private String portalId;
    private String name;
    private String url;



    public Portal(
        String portalId,        String name,        String url    ) {
        this.portalId = portalId;
        this.name = name;
        this.url = url;
    }


    public String getPortalid() {
        return portalId;
    }

    public void setPortalid(String portalId) {
        this.portalId = portalId;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }


}