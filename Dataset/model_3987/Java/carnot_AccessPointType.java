





import java.util.List;
import java.util.ArrayList;

public class carnot_AccessPointType extends IIdentifiableModelElement, ITypedElement {

    private String direction;





    private carnot_IAccessPointOwner carnot_iaccesspointowner;


    public carnot_AccessPointType(
        String direction    ) {
        super(
        );
        this.direction = direction;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }

    public carnot_IAccessPointOwner getCarnot_iaccesspointowner() {
        return carnot_iaccesspointowner;
    }

    public void setCarnot_iaccesspointowner(carnot_IAccessPointOwner carnot_iaccesspointowner) {
        this.carnot_iaccesspointowner = carnot_iaccesspointowner;
    }

}