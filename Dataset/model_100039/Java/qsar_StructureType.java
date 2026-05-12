





import java.util.List;
import java.util.ArrayList;

public class qsar_StructureType  {

    private String resourceid;
    private String has2d;
    private String resourceindex;
    private String has3d;
    private String inchi;
    private String problem;
    private String id;





    private qsar_ResourceType qsar_resourcetype;


    public qsar_StructureType(
        String resourceid,        String has2d,        String resourceindex,        String has3d,        String inchi,        String problem,        String id    ) {
        this.resourceid = resourceid;
        this.has2d = has2d;
        this.resourceindex = resourceindex;
        this.has3d = has3d;
        this.inchi = inchi;
        this.problem = problem;
        this.id = id;
    }


    public String getResourceid() {
        return resourceid;
    }

    public void setResourceid(String resourceid) {
        this.resourceid = resourceid;
    }
    public String getHas2d() {
        return has2d;
    }

    public void setHas2d(String has2d) {
        this.has2d = has2d;
    }
    public String getResourceindex() {
        return resourceindex;
    }

    public void setResourceindex(String resourceindex) {
        this.resourceindex = resourceindex;
    }
    public String getHas3d() {
        return has3d;
    }

    public void setHas3d(String has3d) {
        this.has3d = has3d;
    }
    public String getInchi() {
        return inchi;
    }

    public void setInchi(String inchi) {
        this.inchi = inchi;
    }
    public String getProblem() {
        return problem;
    }

    public void setProblem(String problem) {
        this.problem = problem;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public qsar_ResourceType getQsar_resourcetype() {
        return qsar_resourcetype;
    }

    public void setQsar_resourcetype(qsar_ResourceType qsar_resourcetype) {
        this.qsar_resourcetype = qsar_resourcetype;
    }

}