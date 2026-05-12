





import java.util.List;
import java.util.ArrayList;

public class Spot  {

    private None status;
    private int level;
    private String section;
    private None spotType;
    private boolean covered;
    private boolean isValet;
    private int spotNumber;
    private boolean isDisabledSpot;





    private ParkingLot parkinglot;


    public Spot(
        None status,        int level,        String section,        None spotType,        boolean covered,        boolean isValet,        int spotNumber,        boolean isDisabledSpot    ) {
        this.status = status;
        this.level = level;
        this.section = section;
        this.spotType = spotType;
        this.covered = covered;
        this.isValet = isValet;
        this.spotNumber = spotNumber;
        this.isDisabledSpot = isDisabledSpot;
    }


    public None getStatus() {
        return status;
    }

    public void setStatus(None status) {
        this.status = status;
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
    public None getSpottype() {
        return spotType;
    }

    public void setSpottype(None spotType) {
        this.spotType = spotType;
    }
    public boolean getCovered() {
        return covered;
    }

    public void setCovered(boolean covered) {
        this.covered = covered;
    }
    public boolean getIsvalet() {
        return isValet;
    }

    public void setIsvalet(boolean isValet) {
        this.isValet = isValet;
    }
    public int getSpotnumber() {
        return spotNumber;
    }

    public void setSpotnumber(int spotNumber) {
        this.spotNumber = spotNumber;
    }
    public boolean getIsdisabledspot() {
        return isDisabledSpot;
    }

    public void setIsdisabledspot(boolean isDisabledSpot) {
        this.isDisabledSpot = isDisabledSpot;
    }

    public ParkingLot getParkinglot() {
        return parkinglot;
    }

    public void setParkinglot(ParkingLot parkinglot) {
        this.parkinglot = parkinglot;
    }

}