





import java.util.List;
import java.util.ArrayList;

public class EA_Model_RoadTrafficAccident  {

    private int fatalvictims;





    private List<EA_Model_CrashedVehicle> ea_model_crashedvehicles;




    private EA_Model_RoadwayWithAccident ea_model_roadwaywithaccident;




    private EA_Model_CrashedVehicle ea_model_crashedvehicle;




    private EA_Model_RoadwayWithAccident ea_model_roadwaywithaccident;


    public EA_Model_RoadTrafficAccident(
        int fatalvictims    ) {
        this.fatalvictims = fatalvictims;
        this.ea_model_crashedvehicles = new ArrayList<>();
    }

    public EA_Model_RoadTrafficAccident(
        int fatalvictims        ArrayList<EA_Model_CrashedVehicle> ea_model_crashedvehicles    ) {
        this.fatalvictims = fatalvictims;
        this.ea_model_crashedvehicles = ea_model_crashedvehicles;
    }

    public int getFatalvictims() {
        return fatalvictims;
    }

    public void setFatalvictims(int fatalvictims) {
        this.fatalvictims = fatalvictims;
    }

    public List<EA_Model_CrashedVehicle> getEa_model_crashedvehicles() {
        return ea_model_crashedvehicles;
    }

    public void addEa_model_crashedvehicle(Ea_model_crashedvehicle ea_model_crashedvehicle) {
        this.ea_model_crashedvehicles.add(ea_model_crashedvehicle);
    }
    public EA_Model_RoadwayWithAccident getEa_model_roadwaywithaccident() {
        return ea_model_roadwaywithaccident;
    }

    public void setEa_model_roadwaywithaccident(EA_Model_RoadwayWithAccident ea_model_roadwaywithaccident) {
        this.ea_model_roadwaywithaccident = ea_model_roadwaywithaccident;
    }
    public EA_Model_CrashedVehicle getEa_model_crashedvehicle() {
        return ea_model_crashedvehicle;
    }

    public void setEa_model_crashedvehicle(EA_Model_CrashedVehicle ea_model_crashedvehicle) {
        this.ea_model_crashedvehicle = ea_model_crashedvehicle;
    }
    public EA_Model_RoadwayWithAccident getEa_model_roadwaywithaccident() {
        return ea_model_roadwaywithaccident;
    }

    public void setEa_model_roadwaywithaccident(EA_Model_RoadwayWithAccident ea_model_roadwaywithaccident) {
        this.ea_model_roadwaywithaccident = ea_model_roadwaywithaccident;
    }

}