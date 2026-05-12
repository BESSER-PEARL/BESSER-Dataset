





import java.util.List;
import java.util.ArrayList;

public class Parking_Record  {

    private String vehicleColor;
    private String vehicleModel;
    private String releaseTime;
    private int hourlyRate;
    private String vehicleLicensePlate;
    private String parkTime;
    private String ownerName;
    private String ownerPhone;
    private None spot;
    private int totalCost;





    private ParkingLot parkinglot;




    private Spot spot;


    public Parking_Record(
        String vehicleColor,        String vehicleModel,        String releaseTime,        int hourlyRate,        String vehicleLicensePlate,        String parkTime,        String ownerName,        String ownerPhone,        None spot,        int totalCost    ) {
        this.vehicleColor = vehicleColor;
        this.vehicleModel = vehicleModel;
        this.releaseTime = releaseTime;
        this.hourlyRate = hourlyRate;
        this.vehicleLicensePlate = vehicleLicensePlate;
        this.parkTime = parkTime;
        this.ownerName = ownerName;
        this.ownerPhone = ownerPhone;
        this.spot = spot;
        this.totalCost = totalCost;
    }


    public String getVehiclecolor() {
        return vehicleColor;
    }

    public void setVehiclecolor(String vehicleColor) {
        this.vehicleColor = vehicleColor;
    }
    public String getVehiclemodel() {
        return vehicleModel;
    }

    public void setVehiclemodel(String vehicleModel) {
        this.vehicleModel = vehicleModel;
    }
    public String getReleasetime() {
        return releaseTime;
    }

    public void setReleasetime(String releaseTime) {
        this.releaseTime = releaseTime;
    }
    public int getHourlyrate() {
        return hourlyRate;
    }

    public void setHourlyrate(int hourlyRate) {
        this.hourlyRate = hourlyRate;
    }
    public String getVehiclelicenseplate() {
        return vehicleLicensePlate;
    }

    public void setVehiclelicenseplate(String vehicleLicensePlate) {
        this.vehicleLicensePlate = vehicleLicensePlate;
    }
    public String getParktime() {
        return parkTime;
    }

    public void setParktime(String parkTime) {
        this.parkTime = parkTime;
    }
    public String getOwnername() {
        return ownerName;
    }

    public void setOwnername(String ownerName) {
        this.ownerName = ownerName;
    }
    public String getOwnerphone() {
        return ownerPhone;
    }

    public void setOwnerphone(String ownerPhone) {
        this.ownerPhone = ownerPhone;
    }
    public None getSpot() {
        return spot;
    }

    public void setSpot(None spot) {
        this.spot = spot;
    }
    public int getTotalcost() {
        return totalCost;
    }

    public void setTotalcost(int totalCost) {
        this.totalCost = totalCost;
    }

    public ParkingLot getParkinglot() {
        return parkinglot;
    }

    public void setParkinglot(ParkingLot parkinglot) {
        this.parkinglot = parkinglot;
    }
    public Spot getSpot() {
        return spot;
    }

    public void setSpot(Spot spot) {
        this.spot = spot;
    }

}