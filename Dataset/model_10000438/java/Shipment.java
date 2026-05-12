




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Shipment  {

    private String SippingType;
    private String Forbidden_to_ship;
    private int pireodofShip;
    private LocalDate Date;





    private List<Costomer> costomers;


    public Shipment(
        String SippingType,        String Forbidden_to_ship,        int pireodofShip,        LocalDate Date    ) {
        this.SippingType = SippingType;
        this.Forbidden_to_ship = Forbidden_to_ship;
        this.pireodofShip = pireodofShip;
        this.Date = Date;
        this.costomers = new ArrayList<>();
    }

    public Shipment(
        String SippingType,        String Forbidden_to_ship,        int pireodofShip,        LocalDate Date        ArrayList<Costomer> costomers    ) {
        this.SippingType = SippingType;
        this.Forbidden_to_ship = Forbidden_to_ship;
        this.pireodofShip = pireodofShip;
        this.Date = Date;
        this.costomers = costomers;
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
    public int getPireodofship() {
        return pireodofShip;
    }

    public void setPireodofship(int pireodofShip) {
        this.pireodofShip = pireodofShip;
    }
    public LocalDate getDate() {
        return Date;
    }

    public void setDate(LocalDate Date) {
        this.Date = Date;
    }

    public List<Costomer> getCostomers() {
        return costomers;
    }

    public void addCostomer(Costomer costomer) {
        this.costomers.add(costomer);
    }

}