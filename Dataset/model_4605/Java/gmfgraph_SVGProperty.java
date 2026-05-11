





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_SVGProperty  {

    private String setter;
    private String type;
    private String getter;
    private boolean callSuper;
    private String query;
    private String attribute;





    private gmfgraph_SVGFigure gmfgraph_svgfigure;


    public gmfgraph_SVGProperty(
        String setter,        String type,        String getter,        boolean callSuper,        String query,        String attribute    ) {
        this.setter = setter;
        this.type = type;
        this.getter = getter;
        this.callSuper = callSuper;
        this.query = query;
        this.attribute = attribute;
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
    public String getGetter() {
        return getter;
    }

    public void setGetter(String getter) {
        this.getter = getter;
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
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }

    public gmfgraph_SVGFigure getGmfgraph_svgfigure() {
        return gmfgraph_svgfigure;
    }

    public void setGmfgraph_svgfigure(gmfgraph_SVGFigure gmfgraph_svgfigure) {
        this.gmfgraph_svgfigure = gmfgraph_svgfigure;
    }

}