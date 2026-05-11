





import java.util.List;
import java.util.ArrayList;

public class notation_RoutingStyle extends Style {

    private String jumpLinkType;
    private boolean avoidObstructions;
    private String routing;
    private String jumpLinkStatus;
    private String smoothness;
    private boolean closestDistance;
    private int roundedBendpointsRadius;
    private boolean jumpLinksReverse;



    public notation_RoutingStyle(
        String jumpLinkType,        boolean avoidObstructions,        String routing,        String jumpLinkStatus,        String smoothness,        boolean closestDistance,        int roundedBendpointsRadius,        boolean jumpLinksReverse    ) {
        super(
        );
        this.jumpLinkType = jumpLinkType;
        this.avoidObstructions = avoidObstructions;
        this.routing = routing;
        this.jumpLinkStatus = jumpLinkStatus;
        this.smoothness = smoothness;
        this.closestDistance = closestDistance;
        this.roundedBendpointsRadius = roundedBendpointsRadius;
        this.jumpLinksReverse = jumpLinksReverse;
    }


    public String getJumplinktype() {
        return jumpLinkType;
    }

    public void setJumplinktype(String jumpLinkType) {
        this.jumpLinkType = jumpLinkType;
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
    public boolean getClosestdistance() {
        return closestDistance;
    }

    public void setClosestdistance(boolean closestDistance) {
        this.closestDistance = closestDistance;
    }
    public int getRoundedbendpointsradius() {
        return roundedBendpointsRadius;
    }

    public void setRoundedbendpointsradius(int roundedBendpointsRadius) {
        this.roundedBendpointsRadius = roundedBendpointsRadius;
    }
    public boolean getJumplinksreverse() {
        return jumpLinksReverse;
    }

    public void setJumplinksreverse(boolean jumpLinksReverse) {
        this.jumpLinksReverse = jumpLinksReverse;
    }


}