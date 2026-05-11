





import java.util.List;
import java.util.ArrayList;

public class fair_Exhibit  {

    private String comments;
    private int number;
    private boolean inAuction;
    private String award;
    private int salesOrder;
    private String name;



    public fair_Exhibit(
        String comments,        int number,        boolean inAuction,        String award,        int salesOrder,        String name    ) {
        this.comments = comments;
        this.number = number;
        this.inAuction = inAuction;
        this.award = award;
        this.salesOrder = salesOrder;
        this.name = name;
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


}