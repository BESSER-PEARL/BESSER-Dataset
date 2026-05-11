





import java.util.List;
import java.util.ArrayList;

public class notation_RoutingStyle extends RoundedCornersStyle {

    private boolean avoidObstructions;
    private String routing;
    private String jumpLinkType;
    private boolean closestDistance;
    private String jumpLinkStatus;
    private String smoothness;
    private boolean jumpLinksReverse;



    public notation_RoutingStyle(
        boolean avoidObstructions,        String routing,        String jumpLinkType,        boolean closestDistance,        String jumpLinkStatus,        String smoothness,        boolean jumpLinksReverse    ) {
        super(
        );
        this.avoidObstructions = avoidObstructions;
        this.routing = routing;
        this.jumpLinkType = jumpLinkType;
        this.closestDistance = closestDistance;
        this.jumpLinkStatus = jumpLinkStatus;
        this.smoothness = smoothness;
        this.jumpLinksReverse = jumpLinksReverse;
    }


    public boolean getAvoidobstructions() {
        return avoidObstructions;
    }

    public void setAvoidobstructions(boolean avoidObstructions) {
        this.avoidObstructions = avoidObstructions;
    }
    public String getRouting() {
        return routing;
    }

    public void setRouting(String routing) {
        this.routing = routing;
    }
    public String getJumplinktype() {
        return jumpLinkType;
    }

    public void setJumplinktype(String jumpLinkType) {
        this.jumpLinkType = jumpLinkType;
    }
    public boolean getClosestdistance() {
        return closestDistance;
    }

    public void setClosestdistance(boolean closestDistance) {
        this.closestDistance = closestDistance;
    }
    public String getJumplinkstatus() {
        return jumpLinkStatus;
    }

    public void setJumplinkstatus(String jumpLinkStatus) {
        this.jumpLinkStatus = jumpLinkStatus;
    }
    public String getSmoothness() {
        return smoothness;
    }

    public void setSmoothness(String smoothness) {
        this.smoothness = smoothness;
    }
    public boolean getJumplinksreverse() {
        return jumpLinksReverse;
    }

    public void setJumplinksreverse(boolean jumpLinksReverse) {
        this.jumpLinksReverse = jumpLinksReverse;
    }


}