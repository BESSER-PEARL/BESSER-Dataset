





import java.util.List;
import java.util.ArrayList;

public class wappm_HypertextLayer  {

    private String hyperName;





    private wappm_WebModel wappm_webmodel;


    public wappm_HypertextLayer(
        String hyperName    ) {
        this.hyperName = hyperName;
    }


    public String getHypername() {
        return hyperName;
    }

    public void setHypername(String hyperName) {
        this.hyperName = hyperName;
    }

    public wappm_WebModel getWappm_webmodel() {
        return wappm_webmodel;
    }

    public void setWappm_webmodel(wappm_WebModel wappm_webmodel) {
        this.wappm_webmodel = wappm_webmodel;
    }

}