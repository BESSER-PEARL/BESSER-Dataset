





import java.util.List;
import java.util.ArrayList;

public class fair_Exhibit  {

    private int salesOrder;
    private int number;
    private String name;
    private String comments;
    private boolean inAuction;
    private String award;





    private fair_Person fair_person;


    public fair_Exhibit(
        int salesOrder,        int number,        String name,        String comments,        boolean inAuction,        String award    ) {
        this.salesOrder = salesOrder;
        this.number = number;
        this.name = name;
        this.comments = comments;
        this.inAuction = inAuction;
        this.award = award;
    }


    public int getSalesorder() {
        return salesOrder;
    }

    public void setSalesorder(int salesOrder) {
        this.salesOrder = salesOrder;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
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

    public fair_Person getFair_person() {
        return fair_person;
    }

    public void setFair_person(fair_Person fair_person) {
        this.fair_person = fair_person;
    }

}