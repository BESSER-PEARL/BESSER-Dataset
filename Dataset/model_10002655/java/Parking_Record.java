





import java.util.List;
import java.util.ArrayList;

public class Parking_Record  {

    private String ownerName;
    private String releaseTime;
    private String vehicleLicensePlate;
    private String vehicleModel;
    private None spot;
    private int hourlyRate;
    private String ownerPhone;
    private String parkTime;
    private int totalCost;
    private String vehicleColor;





    private Spot spot;




    private ParkingLot parkinglot;


    public Parking_Record(
        String ownerName,        String releaseTime,        String vehicleLicensePlate,        String vehicleModel,        None spot,        int hourlyRate,        String ownerPhone,        String parkTime,        int totalCost,        String vehicleColor    ) {
        this.ownerName = ownerName;
        this.releaseTime = releaseTime;
        this.vehicleLicensePlate = vehicleLicensePlate;
        this.vehicleModel = vehicleModel;
        this.spot = spot;
        this.hourlyRate = hourlyRate;
        this.ownerPhone = ownerPhone;
        this.parkTime = parkTime;
        this.totalCost = totalCost;
        this.vehicleColor = vehicleColor;
    }


    public String getOwnername() {
        return ownerName;
    }

    public void setOwnername(String ownerName) {
        this.ownerName = ownerName;
    }
    public String getReleasetime() {
        return releaseTime;
    }

    public void setReleasetime(String releaseTime) {
        this.releaseTime = releaseTime;
    }
    public String getVehiclelicenseplate() {
        return vehicleLicensePlate;
    }

    public void setVehiclelicenseplate(String vehicleLicensePlate) {
        this.vehicleLicensePlate = vehicleLicensePlate;
    }
    public String getVehiclemodel() {
        return vehicleModel;
    }

    public void setVehiclemodel(String vehicleModel) {
        this.vehicleModel = vehicleModel;
    }
    public None getSpot() {
        return spot;
    }

    public void setSpot(None spot) {
        this.spot = spot;
    }
    public int getHourlyrate() {
        return hourlyRate;
    }

    public void setHourlyrate(int hourlyRate) {
        this.hourlyRate = hourlyRate;
    }
    public String getOwnerphone() {
        return ownerPhone;
    }

    public void setOwnerphone(String ownerPhone) {
        this.ownerPhone = ownerPhone;
    }
    public String getParktime() {
        return parkTime;
    }

    public void setParktime(String parkTime) {
        this.parkTime = parkTime;
    }
    public int getTotalcost() {
        return totalCost;
    }

    public void setTotalcost(int totalCost) {
        this.totalCost = totalCost;
    }
    public String getVehiclecolor() {
        return vehicleColor;
    }

    public void setVehiclecolor(String vehicleColor) {
        this.vehicleColor = vehicleColor;
    }

    public Spot getSpot() {
        return spot;
    }

    public void setSpot(Spot spot) {
        this.spot = spot;
    }
    public ParkingLot getParkinglot() {
        return parkinglot;
    }

    public void setParkinglot(ParkingLot parkinglot) {
        this.parkinglot = parkinglot;
    }

}