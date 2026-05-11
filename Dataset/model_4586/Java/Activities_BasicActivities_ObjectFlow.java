





import java.util.List;
import java.util.ArrayList;

public class Activities_BasicActivities_ObjectFlow extends ActivityEdge {

    private boolean isControlType;
    private boolean isMultireceive;
    private String ordering;
    private boolean isMulticast;





    private Behavior behavior;




    private Behavior behavior;


    public Activities_BasicActivities_ObjectFlow(
        boolean isControlType,        boolean isMultireceive,        String ordering,        boolean isMulticast    ) {
        super(
        );
        this.isControlType = isControlType;
        this.isMultireceive = isMultireceive;
        this.ordering = ordering;
        this.isMulticast = isMulticast;
    }


    public boolean getIscontroltype() {
        return isControlType;
    }

    public void setIscontroltype(boolean isControlType) {
        this.isControlType = isControlType;
    }
    public boolean getIsmultireceive() {
        return isMultireceive;
    }

    public void setIsmultireceive(boolean isMultireceive) {
        this.isMultireceive = isMultireceive;
    }
    public String getOrdering() {
        return ordering;
    }

    public void setOrdering(String ordering) {
        this.ordering = ordering;
    }
    public boolean getIsmulticast() {
        return isMulticast;
    }

    public void setIsmulticast(boolean isMulticast) {
        this.isMulticast = isMulticast;
    }

    public Behavior getBehavior() {
        return behavior;
    }

    public void setBehavior(Behavior behavior) {
        this.behavior = behavior;
    }
    public Behavior getBehavior() {
        return behavior;
    }

    public void setBehavior(Behavior behavior) {
        this.behavior = behavior;
    }

}