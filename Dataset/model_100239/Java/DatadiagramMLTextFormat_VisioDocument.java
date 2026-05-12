





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLTextFormat_VisioDocument  {

    private String buildnum;
    private String start;
    private String key;
    private String metric;
    private String docLangId;
    private String version;



    public DatadiagramMLTextFormat_VisioDocument(
        String buildnum,        String start,        String key,        String metric,        String docLangId,        String version    ) {
        this.buildnum = buildnum;
        this.start = start;
        this.key = key;
        this.metric = metric;
        this.docLangId = docLangId;
        this.version = version;
    }


    public String getBuildnum() {
        return buildnum;
    }

    public void setBuildnum(String buildnum) {
        this.buildnum = buildnum;
    }
    public String getStart() {
        return start;
    }

    public void setStart(String start) {
        this.start = start;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getMetric() {
        return metric;
    }

    public void setMetric(String metric) {
        this.metric = metric;
    }
    public String getDoclangid() {
        return docLangId;
    }

    public void setDoclangid(String docLangId) {
        this.docLangId = docLangId;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }


}