





import java.util.List;
import java.util.ArrayList;

public class HotelManagementClassDiagram_Customer extends Person {

    private int customerID;
    private int bonusPoints;
    private float rank;
    private String miscInfo;



    public HotelManagementClassDiagram_Customer(
        int customerID,        int bonusPoints,        float rank,        String miscInfo    ) {
        super(
        );
        this.customerID = customerID;
        this.bonusPoints = bonusPoints;
        this.rank = rank;
        this.miscInfo = miscInfo;
    }


    public int getCustomerid() {
        return customerID;
    }

    public void setCustomerid(int customerID) {
        this.customerID = customerID;
    }
    public int getBonuspoints() {
        return bonusPoints;
    }

    public void setBonuspoints(int bonusPoints) {
        this.bonusPoints = bonusPoints;
    }
    public float getRank() {
        return rank;
    }

    public void setRank(float rank) {
        this.rank = rank;
    }
    public String getMiscinfo() {
        return miscInfo;
    }

    public void setMiscinfo(String miscInfo) {
        this.miscInfo = miscInfo;
    }


}