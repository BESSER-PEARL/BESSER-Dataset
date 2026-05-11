





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_pc_system_pc_pc_System extends entity_pc_pc_ComposedProvidingRequiringEntity, entity_pc_pc_Entity {






    private List<QoSAnnotations> qosannotationss;


    public pcm_pc_pc_system_pc_pc_System(
    ) {
        super(
        );
        this.qosannotationss = new ArrayList<>();
    }

    public pcm_pc_pc_system_pc_pc_System(
        ArrayList<QoSAnnotations> qosannotationss    ) {
        this.qosannotationss = qosannotationss;
    }


    public List<QoSAnnotations> getQosannotationss() {
        return qosannotationss;
    }

    public void addQosannotations(Qosannotations qosannotations) {
        this.qosannotationss.add(qosannotations);
    }

}