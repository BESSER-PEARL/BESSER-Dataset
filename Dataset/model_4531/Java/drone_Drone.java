





import java.util.List;
import java.util.ArrayList;

public class drone_Drone extends NamedElement {

    private boolean magnetometer;
    private float maxVoltage;
    private int dataRate;
    private float maxPowerConsumption;
    private boolean gps;
    private float communicationRange;
    private float minVoltage;
    private boolean onBoardObstacleAvoidance;
    private boolean giro;
    private boolean accelerometer;
    private int radioFrequency;
    private boolean barometer;





    private List<drone_Processor> drone_processors;


    public drone_Drone(
        boolean magnetometer,        float maxVoltage,        int dataRate,        float maxPowerConsumption,        boolean gps,        float communicationRange,        float minVoltage,        boolean onBoardObstacleAvoidance,        boolean giro,        boolean accelerometer,        int radioFrequency,        boolean barometer    ) {
        super(
        );
        this.magnetometer = magnetometer;
        this.maxVoltage = maxVoltage;
        this.dataRate = dataRate;
        this.maxPowerConsumption = maxPowerConsumption;
        this.gps = gps;
        this.communicationRange = communicationRange;
        this.minVoltage = minVoltage;
        this.onBoardObstacleAvoidance = onBoardObstacleAvoidance;
        this.giro = giro;
        this.accelerometer = accelerometer;
        this.radioFrequency = radioFrequency;
        this.barometer = barometer;
        this.drone_processors = new ArrayList<>();
    }

    public drone_Drone(
        boolean magnetometer,        float maxVoltage,        int dataRate,        float maxPowerConsumption,        boolean gps,        float communicationRange,        float minVoltage,        boolean onBoardObstacleAvoidance,        boolean giro,        boolean accelerometer,        int radioFrequency,        boolean barometer        ArrayList<drone_Processor> drone_processors    ) {
        this.magnetometer = magnetometer;
        this.maxVoltage = maxVoltage;
        this.dataRate = dataRate;
        this.maxPowerConsumption = maxPowerConsumption;
        this.gps = gps;
        this.communicationRange = communicationRange;
        this.minVoltage = minVoltage;
        this.onBoardObstacleAvoidance = onBoardObstacleAvoidance;
        this.giro = giro;
        this.accelerometer = accelerometer;
        this.radioFrequency = radioFrequency;
        this.barometer = barometer;
        this.drone_processors = drone_processors;
    }

    public boolean getMagnetometer() {
        return magnetometer;
    }

    public void setMagnetometer(boolean magnetometer) {
        this.magnetometer = magnetometer;
    }
    public float getMaxvoltage() {
        return maxVoltage;
    }

    public void setMaxvoltage(float maxVoltage) {
        this.maxVoltage = maxVoltage;
    }
    public int getDatarate() {
        return dataRate;
    }

    public void setDatarate(int dataRate) {
        this.dataRate = dataRate;
    }
    public float getMaxpowerconsumption() {
        return maxPowerConsumption;
    }

    public void setMaxpowerconsumption(float maxPowerConsumption) {
        this.maxPowerConsumption = maxPowerConsumption;
    }
    public boolean getGps() {
        return gps;
    }

    public void setGps(boolean gps) {
        this.gps = gps;
    }
    public float getCommunicationrange() {
        return communicationRange;
    }

    public void setCommunicationrange(float communicationRange) {
        this.communicationRange = communicationRange;
    }
    public float getMinvoltage() {
        return minVoltage;
    }

    public void setMinvoltage(float minVoltage) {
        this.minVoltage = minVoltage;
    }
    public boolean getOnboardobstacleavoidance() {
        return onBoardObstacleAvoidance;
    }

    public void setOnboardobstacleavoidance(boolean onBoardObstacleAvoidance) {
        this.onBoardObstacleAvoidance = onBoardObstacleAvoidance;
    }
    public boolean getGiro() {
        return giro;
    }

    public void setGiro(boolean giro) {
        this.giro = giro;
    }
    public boolean getAccelerometer() {
        return accelerometer;
    }

    public void setAccelerometer(boolean accelerometer) {
        this.accelerometer = accelerometer;
    }
    public int getRadiofrequency() {
        return radioFrequency;
    }

    public void setRadiofrequency(int radioFrequency) {
        this.radioFrequency = radioFrequency;
    }
    public boolean getBarometer() {
        return barometer;
    }

    public void setBarometer(boolean barometer) {
        this.barometer = barometer;
    }

    public List<drone_Processor> getDrone_processors() {
        return drone_processors;
    }

    public void addDrone_processor(Drone_processor drone_processor) {
        this.drone_processors.add(drone_processor);
    }

}