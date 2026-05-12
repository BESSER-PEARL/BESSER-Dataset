




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class DistributionSystem_BoardingPass  {

    private String flight;
    private LocalDate dateOfPurchase;
    private int row;
    private boolean isValidated;
    private int price;
    private int seat;





    private DistributionSystem_Ticket distributionsystem_ticket;


    public DistributionSystem_BoardingPass(
        String flight,        LocalDate dateOfPurchase,        int row,        boolean isValidated,        int price,        int seat    ) {
        this.flight = flight;
        this.dateOfPurchase = dateOfPurchase;
        this.row = row;
        this.isValidated = isValidated;
        this.price = price;
        this.seat = seat;
    }


    public String getFlight() {
        return flight;
    }

    public void setFlight(String flight) {
        this.flight = flight;
    }
    public LocalDate getDateofpurchase() {
        return dateOfPurchase;
    }

    public void setDateofpurchase(LocalDate dateOfPurchase) {
        this.dateOfPurchase = dateOfPurchase;
    }
    public int getRow() {
        return row;
    }

    public void setRow(int row) {
        this.row = row;
    }
    public boolean getIsvalidated() {
        return isValidated;
    }

    public void setIsvalidated(boolean isValidated) {
        this.isValidated = isValidated;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public int getSeat() {
        return seat;
    }

    public void setSeat(int seat) {
        this.seat = seat;
    }

    public DistributionSystem_Ticket getDistributionsystem_ticket() {
        return distributionsystem_ticket;
    }

    public void setDistributionsystem_ticket(DistributionSystem_Ticket distributionsystem_ticket) {
        this.distributionsystem_ticket = distributionsystem_ticket;
    }

}