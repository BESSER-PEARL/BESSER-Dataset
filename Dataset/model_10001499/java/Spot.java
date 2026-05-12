





import java.util.List;
import java.util.ArrayList;

public class Spot  {

    private int level;
    private String section;
    private None status;
    private None spotType;
    private boolean isDisabledSpot;
    private boolean covered;
    private int spotNumber;
    private boolean isValet;





    private ParkingLot parkinglot;


    public Spot(
        int level,        String section,        None status,        None spotType,        boolean isDisabledSpot,        boolean covered,        int spotNumber,        boolean isValet    ) {
        this.level = level;
        this.section = section;
        this.status = status;
        this.spotType = spotType;
        this.isDisabledSpot = isDisabledSpot;
        this.covered = covered;
        this.spotNumber = spotNumber;
        this.isValet = isValet;
    }


    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }
    public String getSection() {
        return section;
    }

    public void setSection(String section) {
        this.section = section;
    }
    public None getStatus() {
        return status;
    }

    public void setStatus(None status) {
        this.status = status;
    }
    public None getSpottype() {
        return spotType;
    }

    public void setSpottype(None spotType) {
        this.spotType = spotType;
    }
    public boolean getIsdisabledspot() {
        return isDisabledSpot;
    }

    public void setIsdisabledspot(boolean isDisabledSpot) {
        this.isDisabledSpot = isDisabledSpot;
    }
    public boolean getCovered() {
        return covered;
    }

    public void setCovered(boolean covered) {
        this.covered = covered;
    }
    public int getSpotnumber() {
        return spotNumber;
    }

    public void setSpotnumber(int spotNumber) {
        this.spotNumber = spotNumber;
    }
    public boolean getIsvalet() {
        return isValet;
    }

    public void setIsvalet(boolean isValet) {
        this.isValet = isValet;
    }

    public ParkingLot getParkinglot() {
        return parkinglot;
    }

    public void setParkinglot(ParkingLot parkinglot) {
        this.parkinglot = parkinglot;
    }

}