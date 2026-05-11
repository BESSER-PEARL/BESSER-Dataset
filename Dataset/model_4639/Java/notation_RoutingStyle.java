





import java.util.List;
import java.util.ArrayList;

public class notation_RoutingStyle extends Style {

    private String jumpLinkStatus;
    private String routing;
    private String smoothness;
    private int roundedBendpointsRadius;
    private boolean jumpLinksReverse;
    private boolean avoidObstructions;
    private boolean closestDistance;
    private String jumpLinkType;



    public notation_RoutingStyle(
        String jumpLinkStatus,        String routing,        String smoothness,        int roundedBendpointsRadius,        boolean jumpLinksReverse,        boolean avoidObstructions,        boolean closestDistance,        String jumpLinkType    ) {
        super(
        );
        this.jumpLinkStatus = jumpLinkStatus;
        this.routing = routing;
        this.smoothness = smoothness;
        this.roundedBendpointsRadius = roundedBendpointsRadius;
        this.jumpLinksReverse = jumpLinksReverse;
        this.avoidObstructions = avoidObstructions;
        this.closestDistance = closestDistance;
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
    public String getSmoothness() {
        return smoothness;
    }

    public void setSmoothness(String smoothness) {
        this.smoothness = smoothness;
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
    public String getJumplinktype() {
        return jumpLinkType;
    }

    public void setJumplinktype(String jumpLinkType) {
        this.jumpLinkType = jumpLinkType;
    }


}