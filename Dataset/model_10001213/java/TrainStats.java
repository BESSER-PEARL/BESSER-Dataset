





import java.util.List;
import java.util.ArrayList;

public class TrainStats  {

    private int passengerCount;
    private String trainService;
    private String fuelAvg;
    private String humidityAvg;
    private String tempAvg;





    private Service service;


    public TrainStats(
        int passengerCount,        String trainService,        String fuelAvg,        String humidityAvg,        String tempAvg    ) {
        this.passengerCount = passengerCount;
        this.trainService = trainService;
        this.fuelAvg = fuelAvg;
        this.humidityAvg = humidityAvg;
        this.tempAvg = tempAvg;
    }


    public int getPassengercount() {
        return passengerCount;
    }

    public void setPassengercount(int passengerCount) {
        this.passengerCount = passengerCount;
    }
    public String getTrainservice() {
        return trainService;
    }

    public void setTrainservice(String trainService) {
        this.trainService = trainService;
    }
    public String getFuelavg() {
        return fuelAvg;
    }

    public void setFuelavg(String fuelAvg) {
        this.fuelAvg = fuelAvg;
    }
    public String getHumidityavg() {
        return humidityAvg;
    }

    public void setHumidityavg(String humidityAvg) {
        this.humidityAvg = humidityAvg;
    }
    public String getTempavg() {
        return tempAvg;
    }

    public void setTempavg(String tempAvg) {
        this.tempAvg = tempAvg;
    }

    public Service getService() {
        return service;
    }

    public void setService(Service service) {
        this.service = service;
    }

}