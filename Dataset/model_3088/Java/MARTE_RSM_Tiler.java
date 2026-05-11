





import java.util.List;
import java.util.ArrayList;

public class MARTE_RSM_Tiler extends LinkTopology {

    private String paving;
    private String fitting;
    private String origin;
    private String tiler;





    private RSM_MARTE_ConnectorEnd rsm_marte_connectorend;


    public MARTE_RSM_Tiler(
        String paving,        String fitting,        String origin,        String tiler    ) {
        super(
        );
        this.paving = paving;
        this.fitting = fitting;
        this.origin = origin;
        this.tiler = tiler;
    }


    public String getPaving() {
        return paving;
    }

    public void setPaving(String paving) {
        this.paving = paving;
    }
    public String getFitting() {
        return fitting;
    }

    public void setFitting(String fitting) {
        this.fitting = fitting;
    }
    public String getOrigin() {
        return origin;
    }

    public void setOrigin(String origin) {
        this.origin = origin;
    }
    public String getTiler() {
        return tiler;
    }

    public void setTiler(String tiler) {
        this.tiler = tiler;
    }

    public RSM_MARTE_ConnectorEnd getRsm_marte_connectorend() {
        return rsm_marte_connectorend;
    }

    public void setRsm_marte_connectorend(RSM_MARTE_ConnectorEnd rsm_marte_connectorend) {
        this.rsm_marte_connectorend = rsm_marte_connectorend;
    }

}