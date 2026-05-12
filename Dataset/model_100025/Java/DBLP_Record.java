





import java.util.List;
import java.util.ArrayList;

public class DBLP_Record  {

    private String mdate;
    private String url;
    private String ee;
    private String key;



    public DBLP_Record(
        String mdate,        String url,        String ee,        String key    ) {
        this.mdate = mdate;
        this.url = url;
        this.ee = ee;
        this.key = key;
    }


    public String getMdate() {
        return mdate;
    }

    public void setMdate(String mdate) {
        this.mdate = mdate;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
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