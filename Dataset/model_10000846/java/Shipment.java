




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Shipment  {

    private int pireodofShip;
    private String Forbidden_to_ship;
    private String SippingType;
    private LocalDate Date;





    private List<Costomer> costomers;


    public Shipment(
        int pireodofShip,        String Forbidden_to_ship,        String SippingType,        LocalDate Date    ) {
        this.pireodofShip = pireodofShip;
        this.Forbidden_to_ship = Forbidden_to_ship;
        this.SippingType = SippingType;
        this.Date = Date;
        this.costomers = new ArrayList<>();
    }

    public Shipment(
        int pireodofShip,        String Forbidden_to_ship,        String SippingType,        LocalDate Date        ArrayList<Costomer> costomers    ) {
        this.pireodofShip = pireodofShip;
        this.Forbidden_to_ship = Forbidden_to_ship;
        this.SippingType = SippingType;
        this.Date = Date;
        this.costomers = costomers;
    }

    public int getPireodofship() {
        return pireodofShip;
    }

    public void setPireodofship(int pireodofShip) {
        this.pireodofShip = pireodofShip;
    }
    public String getForbidden_to_ship() {
        return Forbidden_to_ship;
    }

    public void setForbidden_to_ship(String Forbidden_to_ship) {
        this.Forbidden_to_ship = Forbidden_to_ship;
    }
    public String getSippingtype() {
        return SippingType;
    }

    public void setSippingtype(String SippingType) {
        this.SippingType = SippingType;
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