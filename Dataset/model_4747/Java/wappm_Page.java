





import java.util.List;
import java.util.ArrayList;

public class wappm_Page  {

    private String path;
    private String name;





    private wappm_HypertextLayer wappm_hypertextlayer;


    public wappm_Page(
        String path,        String name    ) {
        this.path = path;
        this.name = name;
    }


    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public wappm_HypertextLayer getWappm_hypertextlayer() {
        return wappm_hypertextlayer;
    }

    public void setWappm_hypertextlayer(wappm_HypertextLayer wappm_hypertextlayer) {
        this.wappm_hypertextlayer = wappm_hypertextlayer;
    }

}