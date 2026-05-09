





import java.util.List;
import java.util.ArrayList;

public class DBLP_Record  {

    private String url;
    private String key;
    private String ee;
    private String mdate;



    public DBLP_Record(
        String url,        String key,        String ee,        String mdate    ) {
        this.url = url;
        this.key = key;
        this.ee = ee;
        this.mdate = mdate;
    }


    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getEe() {
        return ee;
    }

    public void setEe(String ee) {
        this.ee = ee;
    }
    public String getMdate() {
        return mdate;
    }

    public void setMdate(String mdate) {
        this.mdate = mdate;
    }


}