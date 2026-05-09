





import java.util.List;
import java.util.ArrayList;

public class oaam_restrictions_SegregationRestriction extends common_OaamBaseElementA, scenario_VariantDependentElementA, scenario_ModeDependentElementA {

    private boolean dissimilarLocation;
    private boolean dissimilarPowerSource;
    private boolean dissimilarTechnology;
    private boolean dissimilarArea;



    public oaam_restrictions_SegregationRestriction(
        boolean dissimilarLocation,        boolean dissimilarPowerSource,        boolean dissimilarTechnology,        boolean dissimilarArea    ) {
        super(
        );
        this.dissimilarLocation = dissimilarLocation;
        this.dissimilarPowerSource = dissimilarPowerSource;
        this.dissimilarTechnology = dissimilarTechnology;
        this.dissimilarArea = dissimilarArea;
    }


    public boolean getDissimilarlocation() {
        return dissimilarLocation;
    }

    public void setDissimilarlocation(boolean dissimilarLocation) {
        this.dissimilarLocation = dissimilarLocation;
    }
    public boolean getDissimilarpowersource() {
        return dissimilarPowerSource;
    }

    public void setDissimilarpowersource(boolean dissimilarPowerSource) {
        this.dissimilarPowerSource = dissimilarPowerSource;
    }
    public boolean getDissimilartechnology() {
        return dissimilarTechnology;
    }

    public void setDissimilartechnology(boolean dissimilarTechnology) {
        this.dissimilarTechnology = dissimilarTechnology;
    }
    public boolean getDissimilararea() {
        return dissimilarArea;
    }

    public void setDissimilararea(boolean dissimilarArea) {
        this.dissimilarArea = dissimilarArea;
    }


}