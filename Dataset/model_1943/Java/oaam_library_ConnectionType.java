





import java.util.List;
import java.util.ArrayList;

public class oaam_library_ConnectionType extends library_ResourceProviderA, common_OaamBaseElementA, library_ResourceConsumerA {

    private boolean isUnidirectional;
    private boolean isPower;
    private boolean allowsCircles;
    private float maxLength;
    private boolean isInformation;
    private int nJoints;
    private boolean isWireless;
    private int nEndPoints;
    private boolean isSwitched;
    private int nStartingPoints;
    private int maxJointBranches;
    private float maxInterfaceToJointDistance;
    private boolean requiresMaster;
    private boolean directConnectionsAllowed;



    public oaam_library_ConnectionType(
        boolean isUnidirectional,        boolean isPower,        boolean allowsCircles,        float maxLength,        boolean isInformation,        int nJoints,        boolean isWireless,        int nEndPoints,        boolean isSwitched,        int nStartingPoints,        int maxJointBranches,        float maxInterfaceToJointDistance,        boolean requiresMaster,        boolean directConnectionsAllowed    ) {
        super(
        );
        this.isUnidirectional = isUnidirectional;
        this.isPower = isPower;
        this.allowsCircles = allowsCircles;
        this.maxLength = maxLength;
        this.isInformation = isInformation;
        this.nJoints = nJoints;
        this.isWireless = isWireless;
        this.nEndPoints = nEndPoints;
        this.isSwitched = isSwitched;
        this.nStartingPoints = nStartingPoints;
        this.maxJointBranches = maxJointBranches;
        this.maxInterfaceToJointDistance = maxInterfaceToJointDistance;
        this.requiresMaster = requiresMaster;
        this.directConnectionsAllowed = directConnectionsAllowed;
    }


    public boolean getIsunidirectional() {
        return isUnidirectional;
    }

    public void setIsunidirectional(boolean isUnidirectional) {
        this.isUnidirectional = isUnidirectional;
    }
    public boolean getIspower() {
        return isPower;
    }

    public void setIspower(boolean isPower) {
        this.isPower = isPower;
    }
    public boolean getAllowscircles() {
        return allowsCircles;
    }

    public void setAllowscircles(boolean allowsCircles) {
        this.allowsCircles = allowsCircles;
    }
    public float getMaxlength() {
        return maxLength;
    }

    public void setMaxlength(float maxLength) {
        this.maxLength = maxLength;
    }
    public boolean getIsinformation() {
        return isInformation;
    }

    public void setIsinformation(boolean isInformation) {
        this.isInformation = isInformation;
    }
    public int getNjoints() {
        return nJoints;
    }

    public void setNjoints(int nJoints) {
        this.nJoints = nJoints;
    }
    public boolean getIswireless() {
        return isWireless;
    }

    public void setIswireless(boolean isWireless) {
        this.isWireless = isWireless;
    }
    public int getNendpoints() {
        return nEndPoints;
    }

    public void setNendpoints(int nEndPoints) {
        this.nEndPoints = nEndPoints;
    }
    public boolean getIsswitched() {
        return isSwitched;
    }

    public void setIsswitched(boolean isSwitched) {
        this.isSwitched = isSwitched;
    }
    public int getNstartingpoints() {
        return nStartingPoints;
    }

    public void setNstartingpoints(int nStartingPoints) {
        this.nStartingPoints = nStartingPoints;
    }
    public int getMaxjointbranches() {
        return maxJointBranches;
    }

    public void setMaxjointbranches(int maxJointBranches) {
        this.maxJointBranches = maxJointBranches;
    }
    public float getMaxinterfacetojointdistance() {
        return maxInterfaceToJointDistance;
    }

    public void setMaxinterfacetojointdistance(float maxInterfaceToJointDistance) {
        this.maxInterfaceToJointDistance = maxInterfaceToJointDistance;
    }
    public boolean getRequiresmaster() {
        return requiresMaster;
    }

    public void setRequiresmaster(boolean requiresMaster) {
        this.requiresMaster = requiresMaster;
    }
    public boolean getDirectconnectionsallowed() {
        return directConnectionsAllowed;
    }

    public void setDirectconnectionsallowed(boolean directConnectionsAllowed) {
        this.directConnectionsAllowed = directConnectionsAllowed;
    }


}