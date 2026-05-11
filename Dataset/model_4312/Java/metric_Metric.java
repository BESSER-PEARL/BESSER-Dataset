





import java.util.List;
import java.util.ArrayList;

public class metric_Metric  {

    private String code;
    private String description;
    private String name;





    private metric_Container metric_container;


    public metric_Metric(
        String code,        String description,        String name    ) {
        this.code = code;
        this.description = description;
        this.name = name;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public metric_Container getMetric_container() {
        return metric_container;
    }

    public void setMetric_container(metric_Container metric_container) {
        this.metric_container = metric_container;
    }

}