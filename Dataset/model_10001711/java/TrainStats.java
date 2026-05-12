





import java.util.List;
import java.util.ArrayList;

public class TrainStats  {

    private String tempAvg;
    private String trainService;
    private int passengerCount;
    private String humidityAvg;
    private String fuelAvg;





    private Service service;


    public TrainStats(
        String tempAvg,        String trainService,        int passengerCount,        String humidityAvg,        String fuelAvg    ) {
        this.tempAvg = tempAvg;
        this.trainService = trainService;
        this.passengerCount = passengerCount;
        this.humidityAvg = humidityAvg;
        this.fuelAvg = fuelAvg;
    }


    public String getTempavg() {
        return tempAvg;
    }

    public void setTempavg(String tempAvg) {
        this.tempAvg = tempAvg;
    }
    public String getTrainservice() {
        return trainService;
    }

    public void setTrainservice(String trainService) {
        this.trainService = trainService;
    }
    public int getPassengercount() {
        return passengerCount;
    }

    public void setPassengercount(int passengerCount) {
        this.passengerCount = passengerCount;
    }
    public String getHumidityavg() {
        return humidityAvg;
    }

    public void setHumidityavg(String humidityAvg) {
        this.humidityAvg = humidityAvg;
    }
    public String getFuelavg() {
        return fuelAvg;
    }

    public void setFuelavg(String fuelAvg) {
        this.fuelAvg = fuelAvg;
    }

    public Service getService() {
        return service;
    }

    public void setService(Service service) {
        this.service = service;
    }

}