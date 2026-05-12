





import java.util.List;
import java.util.ArrayList;

public class TreatmentList  {

    private float treatmentPrice;
    private int treatmentID;
    private String treatmentName;



    public TreatmentList(
        float treatmentPrice,        int treatmentID,        String treatmentName    ) {
        this.treatmentPrice = treatmentPrice;
        this.treatmentID = treatmentID;
        this.treatmentName = treatmentName;
    }


    public float getTreatmentprice() {
        return treatmentPrice;
    }

    public void setTreatmentprice(float treatmentPrice) {
        this.treatmentPrice = treatmentPrice;
    }
    public int getTreatmentid() {
        return treatmentID;
    }

    public void setTreatmentid(int treatmentID) {
        this.treatmentID = treatmentID;
    }
    public String getTreatmentname() {
        return treatmentName;
    }

    public void setTreatmentname(String treatmentName) {
        this.treatmentName = treatmentName;
    }


}