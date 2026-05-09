





import java.util.List;
import java.util.ArrayList;

public class graphbt_Behavior  {

    private String behaviorDesc;
    private String behaviorType;
    private String behaviorRef;
    private String technicalDetail;
    private String behaviorName;





    private graphbt_Component graphbt_component;


    public graphbt_Behavior(
        String behaviorDesc,        String behaviorType,        String behaviorRef,        String technicalDetail,        String behaviorName    ) {
        this.behaviorDesc = behaviorDesc;
        this.behaviorType = behaviorType;
        this.behaviorRef = behaviorRef;
        this.technicalDetail = technicalDetail;
        this.behaviorName = behaviorName;
    }


    public String getBehaviordesc() {
        return behaviorDesc;
    }

    public void setBehaviordesc(String behaviorDesc) {
        this.behaviorDesc = behaviorDesc;
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
    public String getTechnicaldetail() {
        return technicalDetail;
    }

    public void setTechnicaldetail(String technicalDetail) {
        this.technicalDetail = technicalDetail;
    }
    public String getBehaviorname() {
        return behaviorName;
    }

    public void setBehaviorname(String behaviorName) {
        this.behaviorName = behaviorName;
    }

    public graphbt_Component getGraphbt_component() {
        return graphbt_component;
    }

    public void setGraphbt_component(graphbt_Component graphbt_component) {
        this.graphbt_component = graphbt_component;
    }

}