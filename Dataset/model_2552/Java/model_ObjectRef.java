





import java.util.List;
import java.util.ArrayList;

public class model_ObjectRef  {

    private String nature;
    private String type;
    private int domain;
    private String labels;
    private String id;
    private String state;
    private String appId;





    private model_TreeNode model_treenode;


    public model_ObjectRef(
        String nature,        String type,        int domain,        String labels,        String id,        String state,        String appId    ) {
        this.nature = nature;
        this.type = type;
        this.domain = domain;
        this.labels = labels;
        this.id = id;
        this.state = state;
        this.appId = appId;
    }


    public String getNature() {
        return nature;
    }

    public void setNature(String nature) {
        this.nature = nature;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getDomain() {
        return domain;
    }

    public void setDomain(int domain) {
        this.domain = domain;
    }
    public String getLabels() {
        return labels;
    }

    public void setLabels(String labels) {
        this.labels = labels;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getAppid() {
        return appId;
    }

    public void setAppid(String appId) {
        this.appId = appId;
    }

    public model_TreeNode getModel_treenode() {
        return model_treenode;
    }

    public void setModel_treenode(model_TreeNode model_treenode) {
        this.model_treenode = model_treenode;
    }

}