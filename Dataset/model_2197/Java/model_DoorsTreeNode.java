





import java.util.List;
import java.util.ArrayList;

public class model_DoorsTreeNode  {

    private String fullName;
    private String name;
    private String fullNameSegments;





    private List<model_AttributeMap> model_attributemaps;




    private model_DoorsTreeNode model_doorstreenode;




    private model_DoorsTreeNode model_doorstreenode;


    public model_DoorsTreeNode(
        String fullName,        String name,        String fullNameSegments    ) {
        this.fullName = fullName;
        this.name = name;
        this.fullNameSegments = fullNameSegments;
        this.model_attributemaps = new ArrayList<>();
    }

    public model_DoorsTreeNode(
        String fullName,        String name,        String fullNameSegments        ArrayList<model_AttributeMap> model_attributemaps    ) {
        this.fullName = fullName;
        this.name = name;
        this.fullNameSegments = fullNameSegments;
        this.model_attributemaps = model_attributemaps;
    }

    public String getFullname() {
        return fullName;
    }

    public void setFullname(String fullName) {
        this.fullName = fullName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFullnamesegments() {
        return fullNameSegments;
    }

    public void setFullnamesegments(String fullNameSegments) {
        this.fullNameSegments = fullNameSegments;
    }

    public List<model_AttributeMap> getModel_attributemaps() {
        return model_attributemaps;
    }

    public void addModel_attributemap(Model_attributemap model_attributemap) {
        this.model_attributemaps.add(model_attributemap);
    }
    public model_DoorsTreeNode getModel_doorstreenode() {
        return model_doorstreenode;
    }

    public void setModel_doorstreenode(model_DoorsTreeNode model_doorstreenode) {
        this.model_doorstreenode = model_doorstreenode;
    }
    public model_DoorsTreeNode getModel_doorstreenode() {
        return model_doorstreenode;
    }

    public void setModel_doorstreenode(model_DoorsTreeNode model_doorstreenode) {
        this.model_doorstreenode = model_doorstreenode;
    }

}