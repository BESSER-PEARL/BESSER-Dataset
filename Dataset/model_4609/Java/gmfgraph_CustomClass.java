





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_CustomClass  {

    private String qualifiedClassName;





    private List<gmfgraph_CustomAttribute> gmfgraph_customattributes;


    public gmfgraph_CustomClass(
        String qualifiedClassName    ) {
        this.qualifiedClassName = qualifiedClassName;
        this.gmfgraph_customattributes = new ArrayList<>();
    }

    public gmfgraph_CustomClass(
        String qualifiedClassName        ArrayList<gmfgraph_CustomAttribute> gmfgraph_customattributes    ) {
        this.qualifiedClassName = qualifiedClassName;
        this.gmfgraph_customattributes = gmfgraph_customattributes;
    }

    public String getQualifiedclassname() {
        return qualifiedClassName;
    }

    public void setQualifiedclassname(String qualifiedClassName) {
        this.qualifiedClassName = qualifiedClassName;
    }

    public List<gmfgraph_CustomAttribute> getGmfgraph_customattributes() {
        return gmfgraph_customattributes;
    }

    public void addGmfgraph_customattribute(Gmfgraph_customattribute gmfgraph_customattribute) {
        this.gmfgraph_customattributes.add(gmfgraph_customattribute);
    }

}