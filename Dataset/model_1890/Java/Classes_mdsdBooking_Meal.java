





import java.util.List;
import java.util.ArrayList;

public class Classes_mdsdBooking_Meal  {

    private String foodType;
    private float price;
    private float amountOfFood;
    private String schedule;



    public Classes_mdsdBooking_Meal(
        String foodType,        float price,        float amountOfFood,        String schedule    ) {
        this.foodType = foodType;
        this.price = price;
        this.amountOfFood = amountOfFood;
        this.schedule = schedule;
    }


    public String getFoodtype() {
        return foodType;
    }

    public void setFoodtype(String foodType) {
        this.foodType = foodType;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public float getAmountoffood() {
        return amountOfFood;
    }

    public void setAmountoffood(float amountOfFood) {
        this.amountOfFood = amountOfFood;
    }
    public String getSchedule() {
        return schedule;
    }

    public void setSchedule(String schedule) {
        this.schedule = schedule;
    }


}