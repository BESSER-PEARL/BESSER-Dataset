





import java.util.List;
import java.util.ArrayList;

public class Bill  {

    private String billID;
    private float ammount;
    private String date;





    private Nurse nurse;


    public Bill(
        String billID,        float ammount,        String date    ) {
        this.billID = billID;
        this.ammount = ammount;
        this.date = date;
    }


    public String getBillid() {
        return billID;
    }

    public void setBillid(String billID) {
        this.billID = billID;
    }
    public float getAmmount() {
        return ammount;
    }

    public void setAmmount(float ammount) {
        this.ammount = ammount;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public Nurse getNurse() {
        return nurse;
    }

    public void setNurse(Nurse nurse) {
        this.nurse = nurse;
    }

}