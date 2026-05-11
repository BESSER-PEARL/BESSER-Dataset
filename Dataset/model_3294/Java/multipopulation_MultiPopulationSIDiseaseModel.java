





import java.util.List;
import java.util.ArrayList;

public class multipopulation_MultiPopulationSIDiseaseModel extends StandardDiseaseModel {

    private float characteristicMixingDistance;
    private float roadNetworkInfectiousProportion;
    private float physicallyAdjacentInfectiousProportion;



    public multipopulation_MultiPopulationSIDiseaseModel(
        float characteristicMixingDistance,        float roadNetworkInfectiousProportion,        float physicallyAdjacentInfectiousProportion    ) {
        super(
        );
        this.characteristicMixingDistance = characteristicMixingDistance;
        this.roadNetworkInfectiousProportion = roadNetworkInfectiousProportion;
        this.physicallyAdjacentInfectiousProportion = physicallyAdjacentInfectiousProportion;
    }


    public float getCharacteristicmixingdistance() {
        return characteristicMixingDistance;
    }

    public void setCharacteristicmixingdistance(float characteristicMixingDistance) {
        this.characteristicMixingDistance = characteristicMixingDistance;
    }
    public float getRoadnetworkinfectiousproportion() {
        return roadNetworkInfectiousProportion;
    }

    public void setRoadnetworkinfectiousproportion(float roadNetworkInfectiousProportion) {
        this.roadNetworkInfectiousProportion = roadNetworkInfectiousProportion;
    }
    public float getPhysicallyadjacentinfectiousproportion() {
        return physicallyAdjacentInfectiousProportion;
    }

    public void setPhysicallyadjacentinfectiousproportion(float physicallyAdjacentInfectiousProportion) {
        this.physicallyAdjacentInfectiousProportion = physicallyAdjacentInfectiousProportion;
    }


}