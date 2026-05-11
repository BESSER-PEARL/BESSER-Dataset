





import java.util.List;
import java.util.ArrayList;

public class wikidb116_querycache  {

    private String qc_value;
    private String qc_namespace;
    private String qc_type;
    private String qc_title;



    public wikidb116_querycache(
        String qc_value,        String qc_namespace,        String qc_type,        String qc_title    ) {
        this.qc_value = qc_value;
        this.qc_namespace = qc_namespace;
        this.qc_type = qc_type;
        this.qc_title = qc_title;
    }


    public String getQc_value() {
        return qc_value;
    }

    public void setQc_value(String qc_value) {
        this.qc_value = qc_value;
    }
    public String getQc_namespace() {
        return qc_namespace;
    }

    public void setQc_namespace(String qc_namespace) {
        this.qc_namespace = qc_namespace;
    }
    public String getQc_type() {
        return qc_type;
    }

    public void setQc_type(String qc_type) {
        this.qc_type = qc_type;
    }
    public String getQc_title() {
        return qc_title;
    }

    public void setQc_title(String qc_title) {
        this.qc_title = qc_title;
    }


}