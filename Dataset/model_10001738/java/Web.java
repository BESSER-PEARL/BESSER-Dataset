





import java.util.List;
import java.util.ArrayList;

public class Web  {

    private int People_;
    private float TempValue;
    private String OwnerData;
    private String HomeLoc;
    private float SmokeValue;





    private Firebase firebase;


    public Web(
        int People_,        float TempValue,        String OwnerData,        String HomeLoc,        float SmokeValue    ) {
        this.People_ = People_;
        this.TempValue = TempValue;
        this.OwnerData = OwnerData;
        this.HomeLoc = HomeLoc;
        this.SmokeValue = SmokeValue;
    }


    public int getPeople_() {
        return People_;
    }

    public void setPeople_(int People_) {
        this.People_ = People_;
    }
    public float getTempvalue() {
        return TempValue;
    }

    public void setTempvalue(float TempValue) {
        this.TempValue = TempValue;
    }
    public String getOwnerdata() {
        return OwnerData;
    }

    public void setOwnerdata(String OwnerData) {
        this.OwnerData = OwnerData;
    }
    public String getHomeloc() {
        return HomeLoc;
    }

    public void setHomeloc(String HomeLoc) {
        this.HomeLoc = HomeLoc;
    }
    public float getSmokevalue() {
        return SmokeValue;
    }

    public void setSmokevalue(float SmokeValue) {
        this.SmokeValue = SmokeValue;
    }

    public Firebase getFirebase() {
        return firebase;
    }

    public void setFirebase(Firebase firebase) {
        this.firebase = firebase;
    }

}