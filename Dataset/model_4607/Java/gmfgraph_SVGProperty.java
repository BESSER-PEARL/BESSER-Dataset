





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_SVGProperty  {

    private String getter;
    private boolean callSuper;
    private String attribute;
    private String query;
    private String type;
    private String setter;





    private gmfgraph_SVGFigure gmfgraph_svgfigure;


    public gmfgraph_SVGProperty(
        String getter,        boolean callSuper,        String attribute,        String query,        String type,        String setter    ) {
        this.getter = getter;
        this.callSuper = callSuper;
        this.attribute = attribute;
        this.query = query;
        this.type = type;
        this.setter = setter;
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
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getQuery() {
        return query;
    }

    public void setQuery(String query) {
        this.query = query;
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

    public gmfgraph_SVGFigure getGmfgraph_svgfigure() {
        return gmfgraph_svgfigure;
    }

    public void setGmfgraph_svgfigure(gmfgraph_SVGFigure gmfgraph_svgfigure) {
        this.gmfgraph_svgfigure = gmfgraph_svgfigure;
    }

}