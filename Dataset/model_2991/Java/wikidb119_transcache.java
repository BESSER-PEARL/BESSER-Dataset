





import java.util.List;
import java.util.ArrayList;

public class wikidb119_transcache  {

    private String tc_url;
    private String tc_contents;
    private String tc_time;



    public wikidb119_transcache(
        String tc_url,        String tc_contents,        String tc_time    ) {
        this.tc_url = tc_url;
        this.tc_contents = tc_contents;
        this.tc_time = tc_time;
    }


    public String getTc_url() {
        return tc_url;
    }

    public void setTc_url(String tc_url) {
        this.tc_url = tc_url;
    }
    public String getTc_contents() {
        return tc_contents;
    }

    public void setTc_contents(String tc_contents) {
        this.tc_contents = tc_contents;
    }
    public String getTc_time() {
        return tc_time;
    }

    public void setTc_time(String tc_time) {
        this.tc_time = tc_time;
    }


}