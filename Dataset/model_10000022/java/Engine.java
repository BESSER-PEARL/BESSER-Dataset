





import java.util.List;
import java.util.ArrayList;

public class Engine  {

    private int power;
    private int volume;
    private int rpm;
    private int weight;
    private String manufacturer;





    private Car1 car1;


    public Engine(
        int power,        int volume,        int rpm,        int weight,        String manufacturer    ) {
        this.power = power;
        this.volume = volume;
        this.rpm = rpm;
        this.weight = weight;
        this.manufacturer = manufacturer;
    }


    public int getPower() {
        return power;
    }

    public void setPower(int power) {
        this.power = power;
    }
    public int getVolume() {
        return volume;
    }

    public void setVolume(int volume) {
        this.volume = volume;
    }
    public int getRpm() {
        return rpm;
    }

    public void setRpm(int rpm) {
        this.rpm = rpm;
    }
    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }
    public String getManufacturer() {
        return manufacturer;
    }

    public void setManufacturer(String manufacturer) {
        this.manufacturer = manufacturer;
    }

    public Car1 getCar1() {
        return car1;
    }

    public void setCar1(Car1 car1) {
        this.car1 = car1;
    }

}