





import java.util.List;
import java.util.ArrayList;

public class wappm_ContentLayer  {

    private String contentName;





    private wappm_WebModel wappm_webmodel;


    public wappm_ContentLayer(
        String contentName    ) {
        this.contentName = contentName;
    }


    public String getContentname() {
        return contentName;
    }

    public void setContentname(String contentName) {
        this.contentName = contentName;
    }

    public wappm_WebModel getWappm_webmodel() {
        return wappm_webmodel;
    }

    public void setWappm_webmodel(wappm_WebModel wappm_webmodel) {
        this.wappm_webmodel = wappm_webmodel;
    }

}