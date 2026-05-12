





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String date;
    private int orderID;
    private String creditCardDetails;
    private String orderNotes;
    private int time;





    private List<MealDeal> mealdeals;




    private Customer customer;




    private Address address;




    private List<Sides> sidess;


    public Order(
        String date,        int orderID,        String creditCardDetails,        String orderNotes,        int time    ) {
        this.date = date;
        this.orderID = orderID;
        this.creditCardDetails = creditCardDetails;
        this.orderNotes = orderNotes;
        this.time = time;
        this.mealdeals = new ArrayList<>();
        this.sidess = new ArrayList<>();
    }

    public Order(
        String date,        int orderID,        String creditCardDetails,        String orderNotes,        int time        ArrayList<MealDeal> mealdeals,        ArrayList<Sides> sidess    ) {
        this.date = date;
        this.orderID = orderID;
        this.creditCardDetails = creditCardDetails;
        this.orderNotes = orderNotes;
        this.time = time;
        this.mealdeals = mealdeals;
        this.sidess = sidess;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public int getOrderid() {
        return orderID;
    }

    public void setOrderid(int orderID) {
        this.orderID = orderID;
    }
    public String getCreditcarddetails() {
        return creditCardDetails;
    }

    public void setCreditcarddetails(String creditCardDetails) {
        this.creditCardDetails = creditCardDetails;
    }
    public String getOrdernotes() {
        return orderNotes;
    }

    public void setOrdernotes(String orderNotes) {
        this.orderNotes = orderNotes;
    }
    public int getTime() {
        return time;
    }

    public void setTime(int time) {
        this.time = time;
    }

    public List<MealDeal> getMealdeals() {
        return mealdeals;
    }

    public void addMealdeal(Mealdeal mealdeal) {
        this.mealdeals.add(mealdeal);
    }
    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }
    public Address getAddress() {
        return address;
    }

    public void setAddress(Address address) {
        this.address = address;
    }
    public List<Sides> getSidess() {
        return sidess;
    }

    public void addSides(Sides sides) {
        this.sidess.add(sides);
    }

}