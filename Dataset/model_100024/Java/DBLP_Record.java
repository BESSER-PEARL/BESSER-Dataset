





import java.util.List;
import java.util.ArrayList;

public class DBLP_Record  {

    private String ee;
    private String key;
    private String url;
    private String mdate;



    public DBLP_Record(
        String ee,        String key,        String url,        String mdate    ) {
        this.ee = ee;
        this.key = key;
        this.url = url;
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


}