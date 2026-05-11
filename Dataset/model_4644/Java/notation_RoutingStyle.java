





import java.util.List;
import java.util.ArrayList;

public class notation_RoutingStyle extends Style {

    private String jumpLinkType;
    private String jumpLinkStatus;
    private boolean avoidObstructions;
    private String smoothness;
    private String routing;
    private boolean jumpLinksReverse;
    private boolean closestDistance;



    public notation_RoutingStyle(
        String jumpLinkType,        String jumpLinkStatus,        boolean avoidObstructions,        String smoothness,        String routing,        boolean jumpLinksReverse,        boolean closestDistance    ) {
        super(
        );
        this.jumpLinkType = jumpLinkType;
        this.jumpLinkStatus = jumpLinkStatus;
        this.avoidObstructions = avoidObstructions;
        this.smoothness = smoothness;
        this.routing = routing;
        this.jumpLinksReverse = jumpLinksReverse;
        this.closestDistance = closestDistance;
    }


    public String getJumplinktype() {
        return jumpLinkType;
    }

    public void setJumplinktype(String jumpLinkType) {
        this.jumpLinkType = jumpLinkType;
    }
    public String getJumplinkstatus() {
        return jumpLinkStatus;
    }

    public void setJumplinkstatus(String jumpLinkStatus) {
        this.jumpLinkStatus = jumpLinkStatus;
    }
    public boolean getAvoidobstructions() {
        return avoidObstructions;
    }

    public void setAvoidobstructions(boolean avoidObstructions) {
        this.avoidObstructions = avoidObstructions;
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
    public boolean getJumplinksreverse() {
        return jumpLinksReverse;
    }

    public void setJumplinksreverse(boolean jumpLinksReverse) {
        this.jumpLinksReverse = jumpLinksReverse;
    }
    public boolean getClosestdistance() {
        return closestDistance;
    }

    public void setClosestdistance(boolean closestDistance) {
        this.closestDistance = closestDistance;
    }


}