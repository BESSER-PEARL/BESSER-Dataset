





import java.util.List;
import java.util.ArrayList;

public class notation_RoutingStyle extends RoundedCornersStyle {

    private String jumpLinkStatus;
    private boolean jumpLinksReverse;
    private String smoothness;
    private String routing;
    private boolean closestDistance;
    private boolean avoidObstructions;
    private String jumpLinkType;



    public notation_RoutingStyle(
        String jumpLinkStatus,        boolean jumpLinksReverse,        String smoothness,        String routing,        boolean closestDistance,        boolean avoidObstructions,        String jumpLinkType    ) {
        super(
        );
        this.jumpLinkStatus = jumpLinkStatus;
        this.jumpLinksReverse = jumpLinksReverse;
        this.smoothness = smoothness;
        this.routing = routing;
        this.closestDistance = closestDistance;
        this.avoidObstructions = avoidObstructions;
        this.jumpLinkType = jumpLinkType;
    }


    public String getJumplinkstatus() {
        return jumpLinkStatus;
    }

    public void setJumplinkstatus(String jumpLinkStatus) {
        this.jumpLinkStatus = jumpLinkStatus;
    }
    public boolean getJumplinksreverse() {
        return jumpLinksReverse;
    }

    public void setJumplinksreverse(boolean jumpLinksReverse) {
        this.jumpLinksReverse = jumpLinksReverse;
    }
    public String getSmoothness() {
        return smoothness;
    }

    public void setSmoothness(String smoothness) {
        this.smoothness = smoothness;
    }
    public String getRouting() {
        return routing;
    }

    public void setRouting(String routing) {
        this.routing = routing;
    }
    public boolean getClosestdistance() {
        return closestDistance;
    }

    public void setClosestdistance(boolean closestDistance) {
        this.closestDistance = closestDistance;
    }
    public boolean getAvoidobstructions() {
        return avoidObstructions;
    }

    public void setAvoidobstructions(boolean avoidObstructions) {
        this.avoidObstructions = avoidObstructions;
    }
    public String getJumplinktype() {
        return jumpLinkType;
    }

    public void setJumplinktype(String jumpLinkType) {
        this.jumpLinkType = jumpLinkType;
    }


}