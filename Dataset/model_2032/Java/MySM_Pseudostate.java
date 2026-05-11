





import java.util.List;
import java.util.ArrayList;

public class MySM_Pseudostate extends Vertex {

    private String kind;
    private String psId;





    private MySM_Region mysm_region;


    public MySM_Pseudostate(
        String kind,        String psId    ) {
        super(
        );
        this.kind = kind;
        this.psId = psId;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getPsid() {
        return psId;
    }

    public void setPsid(String psId) {
        this.psId = psId;
    }

    public MySM_Region getMysm_region() {
        return mysm_region;
    }

    public void setMysm_region(MySM_Region mysm_region) {
        this.mysm_region = mysm_region;
    }

}