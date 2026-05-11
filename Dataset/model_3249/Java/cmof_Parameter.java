





import java.util.List;
import java.util.ArrayList;

public class cmof_Parameter extends MultiplicityElement, TypedElement {

    private String default;
    private String direction;





    private cmof_BehavioralFeature cmof_behavioralfeature;


    public cmof_Parameter(
        String default,        String direction    ) {
        super(
        );
        this.default = default;
        this.direction = direction;
    }


    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }
    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }

    public cmof_BehavioralFeature getCmof_behavioralfeature() {
        return cmof_behavioralfeature;
    }

    public void setCmof_behavioralfeature(cmof_BehavioralFeature cmof_behavioralfeature) {
        this.cmof_behavioralfeature = cmof_behavioralfeature;
    }

}