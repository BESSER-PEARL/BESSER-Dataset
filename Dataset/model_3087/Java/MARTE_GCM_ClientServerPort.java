





import java.util.List;
import java.util.ArrayList;

public class MARTE_GCM_ClientServerPort  {

    private String specificationKind;
    private String kind;
    private String isConjugated;





    private GCM_MARTE_Port gcm_marte_port;


    public MARTE_GCM_ClientServerPort(
        String specificationKind,        String kind,        String isConjugated    ) {
        this.specificationKind = specificationKind;
        this.kind = kind;
        this.isConjugated = isConjugated;
    }


    public String getSpecificationkind() {
        return specificationKind;
    }

    public void setSpecificationkind(String specificationKind) {
        this.specificationKind = specificationKind;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getIsconjugated() {
        return isConjugated;
    }

    public void setIsconjugated(String isConjugated) {
        this.isConjugated = isConjugated;
    }

    public GCM_MARTE_Port getGcm_marte_port() {
        return gcm_marte_port;
    }

    public void setGcm_marte_port(GCM_MARTE_Port gcm_marte_port) {
        this.gcm_marte_port = gcm_marte_port;
    }

}