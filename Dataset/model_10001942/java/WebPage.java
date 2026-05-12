





import java.util.List;
import java.util.ArrayList;

public class WebPage  {

    private String HomeLoc;
    private String OwnerData;
    private int People_;
    private float SmokeValue;
    private float TempValue;





    private Firebase firebase;


    public WebPage(
        String HomeLoc,        String OwnerData,        int People_,        float SmokeValue,        float TempValue    ) {
        this.HomeLoc = HomeLoc;
        this.OwnerData = OwnerData;
        this.People_ = People_;
        this.SmokeValue = SmokeValue;
        this.TempValue = TempValue;
    }


    public String getHomeloc() {
        return HomeLoc;
    }

    public void setHomeloc(String HomeLoc) {
        this.HomeLoc = HomeLoc;
    }
    public String getOwnerdata() {
        return OwnerData;
    }

    public void setOwnerdata(String OwnerData) {
        this.OwnerData = OwnerData;
    }
    public int getPeople_() {
        return People_;
    }

    public void setPeople_(int People_) {
        this.People_ = People_;
    }
    public float getSmokevalue() {
        return SmokeValue;
    }

    public void setSmokevalue(float SmokeValue) {
        this.SmokeValue = SmokeValue;
    }
    public float getTempvalue() {
        return TempValue;
    }

    public void setTempvalue(float TempValue) {
        this.TempValue = TempValue;
    }

    public Firebase getFirebase() {
        return firebase;
    }

    public void setFirebase(Firebase firebase) {
        this.firebase = firebase;
    }

}