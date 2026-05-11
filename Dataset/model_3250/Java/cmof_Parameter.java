





import java.util.List;
import java.util.ArrayList;

public class cmof_Parameter extends TypedElement, MultiplicityElement {

    private String default;
    private String direction;





    private cmof_ValueSpecification cmof_valuespecification;




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

    public cmof_ValueSpecification getCmof_valuespecification() {
        return cmof_valuespecification;
    }

    public void setCmof_valuespecification(cmof_ValueSpecification cmof_valuespecification) {
        this.cmof_valuespecification = cmof_valuespecification;
    }
    public cmof_BehavioralFeature getCmof_behavioralfeature() {
        return cmof_behavioralfeature;
    }

    public void setCmof_behavioralfeature(cmof_BehavioralFeature cmof_behavioralfeature) {
        this.cmof_behavioralfeature = cmof_behavioralfeature;
    }

}