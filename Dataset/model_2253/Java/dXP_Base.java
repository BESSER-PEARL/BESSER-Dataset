





import java.util.List;
import java.util.ArrayList;

public class dXP_Base  {

    private String status;
    private String dateLastModified;
    private String sourceId;





    private List<dXP_Metadata> dxp_metadatas;


    public dXP_Base(
        String status,        String dateLastModified,        String sourceId    ) {
        this.status = status;
        this.dateLastModified = dateLastModified;
        this.sourceId = sourceId;
        this.dxp_metadatas = new ArrayList<>();
    }

    public dXP_Base(
        String status,        String dateLastModified,        String sourceId        ArrayList<dXP_Metadata> dxp_metadatas    ) {
        this.status = status;
        this.dateLastModified = dateLastModified;
        this.sourceId = sourceId;
        this.dxp_metadatas = dxp_metadatas;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getDatelastmodified() {
        return dateLastModified;
    }

    public void setDatelastmodified(String dateLastModified) {
        this.dateLastModified = dateLastModified;
    }
    public String getSourceid() {
        return sourceId;
    }

    public void setSourceid(String sourceId) {
        this.sourceId = sourceId;
    }

    public List<dXP_Metadata> getDxp_metadatas() {
        return dxp_metadatas;
    }

    public void addDxp_metadata(Dxp_metadata dxp_metadata) {
        this.dxp_metadatas.add(dxp_metadata);
    }

}