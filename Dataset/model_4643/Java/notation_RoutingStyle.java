





import java.util.List;
import java.util.ArrayList;

public class notation_RoutingStyle extends RoundedCornersStyle {

    private String jumpLinkStatus;
    private String routing;
    private boolean jumpLinksReverse;
    private boolean avoidObstructions;
    private boolean closestDistance;
    private String smoothness;
    private String jumpLinkType;



    public notation_RoutingStyle(
        String jumpLinkStatus,        String routing,        boolean jumpLinksReverse,        boolean avoidObstructions,        boolean closestDistance,        String smoothness,        String jumpLinkType    ) {
        super(
        );
        this.jumpLinkStatus = jumpLinkStatus;
        this.routing = routing;
        this.jumpLinksReverse = jumpLinksReverse;
        this.avoidObstructions = avoidObstructions;
        this.closestDistance = closestDistance;
        this.smoothness = smoothness;
        this.jumpLinkType = jumpLinkType;
    }


    public String getJumplinkstatus() {
        return jumpLinkStatus;
    }

    public void setJumplinkstatus(String jumpLinkStatus) {
        this.jumpLinkStatus = jumpLinkStatus;
    }
    public String getRouting() {
        return routing;
    }

    public void setRouting(String routing) {
        this.routing = routing;
    }
    public boolean getJumplinksreverse() {
        return jumpLinksReverse;
    }

    public void setJumplinksreverse(boolean jumpLinksReverse) {
        this.jumpLinksReverse = jumpLinksReverse;
    }
    public boolean getAvoidobstructions() {
        return avoidObstructions;
    }

    public void setAvoidobstructions(boolean avoidObstructions) {
        this.avoidObstructions = avoidObstructions;
    }
    public boolean getClosestdistance() {
        return closestDistance;
    }

    public void setClosestdistance(boolean closestDistance) {
        this.closestDistance = closestDistance;
    }
    public String getSmoothness() {
        return smoothness;
    }

    public void setSmoothness(String smoothness) {
        this.smoothness = smoothness;
    }
    public String getJumplinktype() {
        return jumpLinkType;
    }

    public void setJumplinktype(String jumpLinkType) {
        this.jumpLinkType = jumpLinkType;
    }


}