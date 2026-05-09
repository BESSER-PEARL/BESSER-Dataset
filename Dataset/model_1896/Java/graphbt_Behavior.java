





import java.util.List;
import java.util.ArrayList;

public class graphbt_Behavior  {

    private String behaviorName;
    private String technicalDetail;
    private String behaviorType;
    private String behaviorRef;
    private String behaviorDesc;





    private graphbt_Component graphbt_component;


    public graphbt_Behavior(
        String behaviorName,        String technicalDetail,        String behaviorType,        String behaviorRef,        String behaviorDesc    ) {
        this.behaviorName = behaviorName;
        this.technicalDetail = technicalDetail;
        this.behaviorType = behaviorType;
        this.behaviorRef = behaviorRef;
        this.behaviorDesc = behaviorDesc;
    }


    public String getBehaviorname() {
        return behaviorName;
    }

    public void setBehaviorname(String behaviorName) {
        this.behaviorName = behaviorName;
    }
    public String getTechnicaldetail() {
        return technicalDetail;
    }

    public void setTechnicaldetail(String technicalDetail) {
        this.technicalDetail = technicalDetail;
    }
    public String getBehaviortype() {
        return behaviorType;
    }

    public void setBehaviortype(String behaviorType) {
        this.behaviorType = behaviorType;
    }
    public String getBehaviorref() {
        return behaviorRef;
    }

    public void setBehaviorref(String behaviorRef) {
        this.behaviorRef = behaviorRef;
    }
    public String getBehaviordesc() {
        return behaviorDesc;
    }

    public void setBehaviordesc(String behaviorDesc) {
        this.behaviorDesc = behaviorDesc;
    }

    public graphbt_Component getGraphbt_component() {
        return graphbt_component;
    }

    public void setGraphbt_component(graphbt_Component graphbt_component) {
        this.graphbt_component = graphbt_component;
    }

}