





import java.util.List;
import java.util.ArrayList;

public class qsar_StructureType  {

    private String id;
    private String resourceid;
    private String resourceindex;
    private String inchi;





    private qsar_ResourceType qsar_resourcetype;


    public qsar_StructureType(
        String id,        String resourceid,        String resourceindex,        String inchi    ) {
        this.id = id;
        this.resourceid = resourceid;
        this.resourceindex = resourceindex;
        this.inchi = inchi;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getResourceid() {
        return resourceid;
    }

    public void setResourceid(String resourceid) {
        this.resourceid = resourceid;
    }
    public String getResourceindex() {
        return resourceindex;
    }

    public void setResourceindex(String resourceindex) {
        this.resourceindex = resourceindex;
    }
    public String getInchi() {
        return inchi;
    }

    public void setInchi(String inchi) {
        this.inchi = inchi;
    }

    public qsar_ResourceType getQsar_resourcetype() {
        return qsar_resourcetype;
    }

    public void setQsar_resourcetype(qsar_ResourceType qsar_resourcetype) {
        this.qsar_resourcetype = qsar_resourcetype;
    }

}