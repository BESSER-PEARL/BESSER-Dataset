





import java.util.List;
import java.util.ArrayList;

public class TrainStats  {

    private String humidityAvg;
    private int passengerCount;
    private String tempAvg;
    private String trainService;
    private String fuelAvg;





    private Service service;


    public TrainStats(
        String humidityAvg,        int passengerCount,        String tempAvg,        String trainService,        String fuelAvg    ) {
        this.humidityAvg = humidityAvg;
        this.passengerCount = passengerCount;
        this.tempAvg = tempAvg;
        this.trainService = trainService;
        this.fuelAvg = fuelAvg;
    }


    public String getHumidityavg() {
        return humidityAvg;
    }

    public void setHumidityavg(String humidityAvg) {
        this.humidityAvg = humidityAvg;
    }
    public int getPassengercount() {
        return passengerCount;
    }

    public void setPassengercount(int passengerCount) {
        this.passengerCount = passengerCount;
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