





import java.util.List;
import java.util.ArrayList;

public class SMVC_Link  {

    private String url;





    private SMVC_Page smvc_page;


    public SMVC_Link(
        String url    ) {
        this.url = url;
    }


    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public SMVC_Page getSmvc_page() {
        return smvc_page;
    }

    public void setSmvc_page(SMVC_Page smvc_page) {
        this.smvc_page = smvc_page;
    }

}