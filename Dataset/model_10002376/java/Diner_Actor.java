





import java.util.List;
import java.util.ArrayList;

public class Diner_Actor  {






    private Pay_for_food_UseCase1 pay_for_food_usecase1;




    private Order_food_UseCase1 order_food_usecase1;


    public Diner_Actor(
    ) {
    }



    public Pay_for_food_UseCase1 getPay_for_food_usecase1() {
        return pay_for_food_usecase1;
    }

    public void setPay_for_food_usecase1(Pay_for_food_UseCase1 pay_for_food_usecase1) {
        this.pay_for_food_usecase1 = pay_for_food_usecase1;
    }
    public Order_food_UseCase1 getOrder_food_usecase1() {
        return order_food_usecase1;
    }

    public void setOrder_food_usecase1(Order_food_UseCase1 order_food_usecase1) {
        this.order_food_usecase1 = order_food_usecase1;
    }

}