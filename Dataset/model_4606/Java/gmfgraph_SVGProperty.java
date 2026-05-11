





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_SVGProperty  {

    private boolean callSuper;
    private String attribute;
    private String getter;
    private String query;
    private String setter;
    private String type;





    private gmfgraph_SVGFigure gmfgraph_svgfigure;


    public gmfgraph_SVGProperty(
        boolean callSuper,        String attribute,        String getter,        String query,        String setter,        String type    ) {
        this.callSuper = callSuper;
        this.attribute = attribute;
        this.getter = getter;
        this.query = query;
        this.setter = setter;
        this.type = type;
    }


    public boolean getCallsuper() {
        return callSuper;
    }

    public void setCallsuper(boolean callSuper) {
        this.callSuper = callSuper;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getGetter() {
        return getter;
    }

    public void setGetter(String getter) {
        this.getter = getter;
    }
    public String getQuery() {
        return query;
    }

    public void setQuery(String query) {
        this.query = query;
    }
    public String getSetter() {
        return setter;
    }

    public void setSetter(String setter) {
        this.setter = setter;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public gmfgraph_SVGFigure getGmfgraph_svgfigure() {
        return gmfgraph_svgfigure;
    }

    public void setGmfgraph_svgfigure(gmfgraph_SVGFigure gmfgraph_svgfigure) {
        this.gmfgraph_svgfigure = gmfgraph_svgfigure;
    }

}