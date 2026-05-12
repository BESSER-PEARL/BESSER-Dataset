




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Shipment  {

    private LocalDate Date;
    private int pireodofShip;
    private String SippingType;
    private String Forbidden_to_ship;





    private List<Costomer> costomers;


    public Shipment(
        LocalDate Date,        int pireodofShip,        String SippingType,        String Forbidden_to_ship    ) {
        this.Date = Date;
        this.pireodofShip = pireodofShip;
        this.SippingType = SippingType;
        this.Forbidden_to_ship = Forbidden_to_ship;
        this.costomers = new ArrayList<>();
    }

    public Shipment(
        LocalDate Date,        int pireodofShip,        String SippingType,        String Forbidden_to_ship        ArrayList<Costomer> costomers    ) {
        this.Date = Date;
        this.pireodofShip = pireodofShip;
        this.SippingType = SippingType;
        this.Forbidden_to_ship = Forbidden_to_ship;
        this.costomers = costomers;
    }

    public LocalDate getDate() {
        return Date;
    }

    public void setDate(LocalDate Date) {
        this.Date = Date;
    }
    public int getPireodofship() {
        return pireodofShip;
    }

    public void setPireodofship(int pireodofShip) {
        this.pireodofShip = pireodofShip;
    }
    public String getSippingtype() {
        return SippingType;
    }

    public void setSippingtype(String SippingType) {
        this.SippingType = SippingType;
    }
    public String getForbidden_to_ship() {
        return Forbidden_to_ship;
    }

    public void setForbidden_to_ship(String Forbidden_to_ship) {
        this.Forbidden_to_ship = Forbidden_to_ship;
    }

    public List<Costomer> getCostomers() {
        return costomers;
    }

    public void addCostomer(Costomer costomer) {
        this.costomers.add(costomer);
    }

}