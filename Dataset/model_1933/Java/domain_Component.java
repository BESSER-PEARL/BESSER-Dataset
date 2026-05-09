





import java.util.List;
import java.util.ArrayList;

public class domain_Component extends HTMLLayerHolder {

    private String uid;
    private String name;
    private String componentRoot;



    public domain_Component(
        String uid,        String name,        String componentRoot    ) {
        super(
        );
        this.uid = uid;
        this.name = name;
        this.componentRoot = componentRoot;
    }


    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getComponentroot() {
        return componentRoot;
    }

    public void setComponentroot(String componentRoot) {
        this.componentRoot = componentRoot;
    }


}