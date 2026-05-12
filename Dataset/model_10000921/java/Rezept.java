





import java.util.List;
import java.util.ArrayList;

public class Rezept  {

    private None rezeptname;
    private None basis;
    private int basismenge;
    private String attribute2;
    private String attribute;





    private PlaetzchenForm plaetzchenform;


    public Rezept(
        None rezeptname,        None basis,        int basismenge,        String attribute2,        String attribute    ) {
        this.rezeptname = rezeptname;
        this.basis = basis;
        this.basismenge = basismenge;
        this.attribute2 = attribute2;
        this.attribute = attribute;
    }


    public None getRezeptname() {
        return rezeptname;
    }

    public void setRezeptname(None rezeptname) {
        this.rezeptname = rezeptname;
    }
    public None getBasis() {
        return basis;
    }

    public void setBasis(None basis) {
        this.basis = basis;
    }
    public int getBasismenge() {
        return basismenge;
    }

    public void setBasismenge(int basismenge) {
        this.basismenge = basismenge;
    }
    public String getAttribute2() {
        return attribute2;
    }

    public void setAttribute2(String attribute2) {
        this.attribute2 = attribute2;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }

    public PlaetzchenForm getPlaetzchenform() {
        return plaetzchenform;
    }

    public void setPlaetzchenform(PlaetzchenForm plaetzchenform) {
        this.plaetzchenform = plaetzchenform;
    }

}