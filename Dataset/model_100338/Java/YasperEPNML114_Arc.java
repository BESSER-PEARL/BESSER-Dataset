





import java.util.List;
import java.util.ArrayList;

public class YasperEPNML114_Arc  {

    private String target;
    private String group;
    private String source;
    private String id;



    public YasperEPNML114_Arc(
        String target,        String group,        String source,        String id    ) {
        this.target = target;
        this.group = group;
        this.source = source;
        this.id = id;
    }


    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}