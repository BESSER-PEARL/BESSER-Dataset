




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Requisition  {

    private LocalDate date_delivered;
    private LocalDate date_ordered;
    private int num;
    private None supply;
    private int quantity_required;
    private None responsable;
    private None ward;





    private ChargeNurse chargenurse;




    private Ward ward;


    public Requisition(
        LocalDate date_delivered,        LocalDate date_ordered,        int num,        None supply,        int quantity_required,        None responsable,        None ward    ) {
        this.date_delivered = date_delivered;
        this.date_ordered = date_ordered;
        this.num = num;
        this.supply = supply;
        this.quantity_required = quantity_required;
        this.responsable = responsable;
        this.ward = ward;
    }


    public LocalDate getDate_delivered() {
        return date_delivered;
    }

    public void setDate_delivered(LocalDate date_delivered) {
        this.date_delivered = date_delivered;
    }
    public LocalDate getDate_ordered() {
        return date_ordered;
    }

    public void setDate_ordered(LocalDate date_ordered) {
        this.date_ordered = date_ordered;
    }
    public int getNum() {
        return num;
    }

    public void setNum(int num) {
        this.num = num;
    }
    public None getSupply() {
        return supply;
    }

    public void setSupply(None supply) {
        this.supply = supply;
    }
    public int getQuantity_required() {
        return quantity_required;
    }

    public void setQuantity_required(int quantity_required) {
        this.quantity_required = quantity_required;
    }
    public None getResponsable() {
        return responsable;
    }

    public void setResponsable(None responsable) {
        this.responsable = responsable;
    }
    public None getWard() {
        return ward;
    }

    public void setWard(None ward) {
        this.ward = ward;
    }

    public ChargeNurse getChargenurse() {
        return chargenurse;
    }

    public void setChargenurse(ChargeNurse chargenurse) {
        this.chargenurse = chargenurse;
    }
    public Ward getWard() {
        return ward;
    }

    public void setWard(Ward ward) {
        this.ward = ward;
    }

}