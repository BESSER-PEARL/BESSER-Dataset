





import java.util.List;
import java.util.ArrayList;

public class MARTE_GCM_ClientServerPort  {

    private String kind;
    private String specificationKind;





    private GCM_MARTE_Port gcm_marte_port;


    public MARTE_GCM_ClientServerPort(
        String kind,        String specificationKind    ) {
        this.kind = kind;
        this.specificationKind = specificationKind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getSpecificationkind() {
        return specificationKind;
    }

    public void setSpecificationkind(String specificationKind) {
        this.specificationKind = specificationKind;
    }

    public GCM_MARTE_Port getGcm_marte_port() {
        return gcm_marte_port;
    }

    public void setGcm_marte_port(GCM_MARTE_Port gcm_marte_port) {
        this.gcm_marte_port = gcm_marte_port;
    }

}