





import java.util.List;
import java.util.ArrayList;

public class standard_SI extends StandardDiseaseModel {

    private float recoveryRate;
    private float characteristicMixingDistance;
    private float infectiousMortality;
    private float transmissionRate;
    private float nonLinearityCoefficient;
    private float roadNetworkInfectiousProportion;
    private float physicallyAdjacentInfectiousProportion;
    private float infectiousMortalityRate;



    public standard_SI(
        float recoveryRate,        float characteristicMixingDistance,        float infectiousMortality,        float transmissionRate,        float nonLinearityCoefficient,        float roadNetworkInfectiousProportion,        float physicallyAdjacentInfectiousProportion,        float infectiousMortalityRate    ) {
        super(
        );
        this.recoveryRate = recoveryRate;
        this.characteristicMixingDistance = characteristicMixingDistance;
        this.infectiousMortality = infectiousMortality;
        this.transmissionRate = transmissionRate;
        this.nonLinearityCoefficient = nonLinearityCoefficient;
        this.roadNetworkInfectiousProportion = roadNetworkInfectiousProportion;
        this.physicallyAdjacentInfectiousProportion = physicallyAdjacentInfectiousProportion;
        this.infectiousMortalityRate = infectiousMortalityRate;
    }


    public float getRecoveryrate() {
        return recoveryRate;
    }

    public void setRecoveryrate(float recoveryRate) {
        this.recoveryRate = recoveryRate;
    }
    public float getCharacteristicmixingdistance() {
        return characteristicMixingDistance;
    }

    public void setCharacteristicmixingdistance(float characteristicMixingDistance) {
        this.characteristicMixingDistance = characteristicMixingDistance;
    }
    public float getInfectiousmortality() {
        return infectiousMortality;
    }

    public void setInfectiousmortality(float infectiousMortality) {
        this.infectiousMortality = infectiousMortality;
    }
    public float getTransmissionrate() {
        return transmissionRate;
    }

    public void setTransmissionrate(float transmissionRate) {
        this.transmissionRate = transmissionRate;
    }
    public float getNonlinearitycoefficient() {
        return nonLinearityCoefficient;
    }

    public void setNonlinearitycoefficient(float nonLinearityCoefficient) {
        this.nonLinearityCoefficient = nonLinearityCoefficient;
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
    public float getInfectiousmortalityrate() {
        return infectiousMortalityRate;
    }

    public void setInfectiousmortalityrate(float infectiousMortalityRate) {
        this.infectiousMortalityRate = infectiousMortalityRate;
    }


}