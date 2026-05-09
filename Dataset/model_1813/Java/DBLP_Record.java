





import java.util.List;
import java.util.ArrayList;

public class DBLP_Record  {

    private String url;
    private String mdate;
    private String ee;
    private String key;



    public DBLP_Record(
        String url,        String mdate,        String ee,        String key    ) {
        this.url = url;
        this.mdate = mdate;
        this.ee = ee;
        this.key = key;
    }


    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getMdate() {
        return mdate;
    }

    public void setMdate(String mdate) {
        this.mdate = mdate;
    }
    public String getEe() {
        return ee;
    }

    public void setEe(String ee) {
        this.ee = ee;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }


}