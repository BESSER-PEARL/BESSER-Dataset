





import java.util.List;
import java.util.ArrayList;

public class fair_Exhibit  {

    private boolean inAuction;
    private String award;
    private String comments;
    private int number;
    private int salesOrder;
    private String name;





    private fair_Lot fair_lot;




    private fair_Lot fair_lot;




    private fair_Person fair_person;




    private fair_Animal fair_animal;


    public fair_Exhibit(
        boolean inAuction,        String award,        String comments,        int number,        int salesOrder,        String name    ) {
        this.inAuction = inAuction;
        this.award = award;
        this.comments = comments;
        this.number = number;
        this.salesOrder = salesOrder;
        this.name = name;
    }


    public boolean getInauction() {
        return inAuction;
    }

    public void setInauction(boolean inAuction) {
        this.inAuction = inAuction;
    }
    public String getAward() {
        return award;
    }

    public void setAward(String award) {
        this.award = award;
    }
    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public int getSalesorder() {
        return salesOrder;
    }

    public void setSalesorder(int salesOrder) {
        this.salesOrder = salesOrder;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fair_Lot getFair_lot() {
        return fair_lot;
    }

    public void setFair_lot(fair_Lot fair_lot) {
        this.fair_lot = fair_lot;
    }
    public fair_Lot getFair_lot() {
        return fair_lot;
    }

    public void setFair_lot(fair_Lot fair_lot) {
        this.fair_lot = fair_lot;
    }
    public fair_Person getFair_person() {
        return fair_person;
    }

    public void setFair_person(fair_Person fair_person) {
        this.fair_person = fair_person;
    }
    public fair_Animal getFair_animal() {
        return fair_animal;
    }

    public void setFair_animal(fair_Animal fair_animal) {
        this.fair_animal = fair_animal;
    }

}