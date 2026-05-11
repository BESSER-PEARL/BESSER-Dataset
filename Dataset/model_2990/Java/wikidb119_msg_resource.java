





import java.util.List;
import java.util.ArrayList;

public class wikidb119_msg_resource  {

    private String mr_blob;
    private String mr_resource;
    private String mr_timestamp;
    private String mr_lang;



    public wikidb119_msg_resource(
        String mr_blob,        String mr_resource,        String mr_timestamp,        String mr_lang    ) {
        this.mr_blob = mr_blob;
        this.mr_resource = mr_resource;
        this.mr_timestamp = mr_timestamp;
        this.mr_lang = mr_lang;
    }


    public String getMr_blob() {
        return mr_blob;
    }

    public void setMr_blob(String mr_blob) {
        this.mr_blob = mr_blob;
    }
    public String getMr_resource() {
        return mr_resource;
    }

    public void setMr_resource(String mr_resource) {
        this.mr_resource = mr_resource;
    }
    public String getMr_timestamp() {
        return mr_timestamp;
    }

    public void setMr_timestamp(String mr_timestamp) {
        this.mr_timestamp = mr_timestamp;
    }
    public String getMr_lang() {
        return mr_lang;
    }

    public void setMr_lang(String mr_lang) {
        this.mr_lang = mr_lang;
    }


}