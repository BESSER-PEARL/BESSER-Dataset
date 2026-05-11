





import java.util.List;
import java.util.ArrayList;

public class wikidb119_interwiki  {

    private String iw_wikiid;
    private String iw_api;
    private String iw_prefix;
    private int iw_local;
    private int iw_trans;
    private String iw_url;



    public wikidb119_interwiki(
        String iw_wikiid,        String iw_api,        String iw_prefix,        int iw_local,        int iw_trans,        String iw_url    ) {
        this.iw_wikiid = iw_wikiid;
        this.iw_api = iw_api;
        this.iw_prefix = iw_prefix;
        this.iw_local = iw_local;
        this.iw_trans = iw_trans;
        this.iw_url = iw_url;
    }


    public String getIw_wikiid() {
        return iw_wikiid;
    }

    public void setIw_wikiid(String iw_wikiid) {
        this.iw_wikiid = iw_wikiid;
    }
    public String getIw_api() {
        return iw_api;
    }

    public void setIw_api(String iw_api) {
        this.iw_api = iw_api;
    }
    public String getIw_prefix() {
        return iw_prefix;
    }

    public void setIw_prefix(String iw_prefix) {
        this.iw_prefix = iw_prefix;
    }
    public int getIw_local() {
        return iw_local;
    }

    public void setIw_local(int iw_local) {
        this.iw_local = iw_local;
    }
    public int getIw_trans() {
        return iw_trans;
    }

    public void setIw_trans(int iw_trans) {
        this.iw_trans = iw_trans;
    }
    public String getIw_url() {
        return iw_url;
    }

    public void setIw_url(String iw_url) {
        this.iw_url = iw_url;
    }


}