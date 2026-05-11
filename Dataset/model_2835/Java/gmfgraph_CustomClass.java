





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_CustomClass  {

    private String qualifiedClassName;
    private String bundleName;



    public gmfgraph_CustomClass(
        String qualifiedClassName,        String bundleName    ) {
        this.qualifiedClassName = qualifiedClassName;
        this.bundleName = bundleName;
    }


    public String getQualifiedclassname() {
        return qualifiedClassName;
    }

    public void setQualifiedclassname(String qualifiedClassName) {
        this.qualifiedClassName = qualifiedClassName;
    }
    public String getBundlename() {
        return bundleName;
    }

    public void setBundlename(String bundleName) {
        this.bundleName = bundleName;
    }


}