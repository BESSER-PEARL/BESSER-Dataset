





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int drinkPrice;
    private String customer;
    private String foodName;
    private int foodPrice;
    private String drinkName;





    private Payment payment;


    public Order(
        int drinkPrice,        String customer,        String foodName,        int foodPrice,        String drinkName    ) {
        this.drinkPrice = drinkPrice;
        this.customer = customer;
        this.foodName = foodName;
        this.foodPrice = foodPrice;
        this.drinkName = drinkName;
    }


    public int getDrinkprice() {
        return drinkPrice;
    }

    public void setDrinkprice(int drinkPrice) {
        this.drinkPrice = drinkPrice;
    }
    public String getCustomer() {
        return customer;
    }

    public void setCustomer(String customer) {
        this.customer = customer;
    }
    public String getFoodname() {
        return foodName;
    }

    public void setFoodname(String foodName) {
        this.foodName = foodName;
    }
    public int getFoodprice() {
        return foodPrice;
    }

    public void setFoodprice(int foodPrice) {
        this.foodPrice = foodPrice;
    }
    public String getDrinkname() {
        return drinkName;
    }

    public void setDrinkname(String drinkName) {
        this.drinkName = drinkName;
    }

    public Payment getPayment() {
        return payment;
    }

    public void setPayment(Payment payment) {
        this.payment = payment;
    }

}