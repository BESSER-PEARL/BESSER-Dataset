





import java.util.List;
import java.util.ArrayList;

public class MARTE_GCM_GCMInvocatingBehavior  {






    private List<GCM_MARTE_InvocationAction> gcm_marte_invocationactions;




    private List<GCM_MARTE_Port> gcm_marte_ports;




    private GCM_MARTE_Behavior gcm_marte_behavior;




    private List<GCM_MARTE_Feature> gcm_marte_features;


    public MARTE_GCM_GCMInvocatingBehavior(
    ) {
        this.gcm_marte_invocationactions = new ArrayList<>();
        this.gcm_marte_ports = new ArrayList<>();
        this.gcm_marte_features = new ArrayList<>();
    }

    public MARTE_GCM_GCMInvocatingBehavior(
        ArrayList<GCM_MARTE_InvocationAction> gcm_marte_invocationactions,        ArrayList<GCM_MARTE_Port> gcm_marte_ports,        ArrayList<GCM_MARTE_Feature> gcm_marte_features    ) {
        this.gcm_marte_invocationactions = gcm_marte_invocationactions;
        this.gcm_marte_ports = gcm_marte_ports;
        this.gcm_marte_features = gcm_marte_features;
    }


    public List<GCM_MARTE_InvocationAction> getGcm_marte_invocationactions() {
        return gcm_marte_invocationactions;
    }

    public void addGcm_marte_invocationaction(Gcm_marte_invocationaction gcm_marte_invocationaction) {
        this.gcm_marte_invocationactions.add(gcm_marte_invocationaction);
    }
    public List<GCM_MARTE_Port> getGcm_marte_ports() {
        return gcm_marte_ports;
    }

    public void addGcm_marte_port(Gcm_marte_port gcm_marte_port) {
        this.gcm_marte_ports.add(gcm_marte_port);
    }
    public GCM_MARTE_Behavior getGcm_marte_behavior() {
        return gcm_marte_behavior;
    }

    public void setGcm_marte_behavior(GCM_MARTE_Behavior gcm_marte_behavior) {
        this.gcm_marte_behavior = gcm_marte_behavior;
    }
    public List<GCM_MARTE_Feature> getGcm_marte_features() {
        return gcm_marte_features;
    }

    public void addGcm_marte_feature(Gcm_marte_feature gcm_marte_feature) {
        this.gcm_marte_features.add(gcm_marte_feature);
    }

}