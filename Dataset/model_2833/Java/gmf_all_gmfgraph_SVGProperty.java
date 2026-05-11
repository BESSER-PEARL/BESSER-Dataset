





import java.util.List;
import java.util.ArrayList;

public class gmf_all_gmfgraph_SVGProperty  {

    private String type;
    private String setter;
    private boolean callSuper;
    private String query;
    private String getter;
    private String attribute;



    public gmf_all_gmfgraph_SVGProperty(
        String type,        String setter,        boolean callSuper,        String query,        String getter,        String attribute    ) {
        this.type = type;
        this.setter = setter;
        this.callSuper = callSuper;
        this.query = query;
        this.getter = getter;
        this.attribute = attribute;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getSetter() {
        return setter;
    }

    public void setSetter(String setter) {
        this.setter = setter;
    }
    public boolean getCallsuper() {
        return callSuper;
    }

    public void setCallsuper(boolean callSuper) {
        this.callSuper = callSuper;
    }
    public String getQuery() {
        return query;
    }

    public void setQuery(String query) {
        this.query = query;
    }
    public String getGetter() {
        return getter;
    }

    public void setGetter(String getter) {
        this.getter = getter;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }


}