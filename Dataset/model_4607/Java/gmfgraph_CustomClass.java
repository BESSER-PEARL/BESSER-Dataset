





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_CustomClass extends CustomAttributeOwner {

    private String qualifiedClassName;



    public gmfgraph_CustomClass(
        String qualifiedClassName    ) {
        super(
        );
        this.qualifiedClassName = qualifiedClassName;
    }


    public String getQualifiedclassname() {
        return qualifiedClassName;
    }

    public void setQualifiedclassname(String qualifiedClassName) {
        this.qualifiedClassName = qualifiedClassName;
    }


}