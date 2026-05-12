





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLBasicDef_VisioDocument  {

    private String version;
    private String key;
    private String metric;
    private String start;
    private String buildnum;
    private String docLangId;



    public DatadiagramMLBasicDef_VisioDocument(
        String version,        String key,        String metric,        String start,        String buildnum,        String docLangId    ) {
        this.version = version;
        this.key = key;
        this.metric = metric;
        this.start = start;
        this.buildnum = buildnum;
        this.docLangId = docLangId;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
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
    public String getStart() {
        return start;
    }

    public void setStart(String start) {
        this.start = start;
    }
    public String getBuildnum() {
        return buildnum;
    }

    public void setBuildnum(String buildnum) {
        this.buildnum = buildnum;
    }
    public String getDoclangid() {
        return docLangId;
    }

    public void setDoclangid(String docLangId) {
        this.docLangId = docLangId;
    }


}