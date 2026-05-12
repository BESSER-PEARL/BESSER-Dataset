





import java.util.List;
import java.util.ArrayList;

public class Travel_Agent_Actor  {






    private Pay_Travel_Agent_UseCase pay_travel_agent_usecase;




    private Register__Login_UseCase register__login_usecase;




    private Proceed_to_Checkout_UseCase proceed_to_checkout_usecase;




    private Review_Order_UseCase review_order_usecase;




    private Make_Payment___Checkout_UseCase make_payment___checkout_usecase;




    private Choose_Flight_UseCase choose_flight_usecase;




    private Check_Tickets_UseCase check_tickets_usecase;


    public Travel_Agent_Actor(
    ) {
    }



    public Pay_Travel_Agent_UseCase getPay_travel_agent_usecase() {
        return pay_travel_agent_usecase;
    }

    public void setPay_travel_agent_usecase(Pay_Travel_Agent_UseCase pay_travel_agent_usecase) {
        this.pay_travel_agent_usecase = pay_travel_agent_usecase;
    }
    public Register__Login_UseCase getRegister__login_usecase() {
        return register__login_usecase;
    }

    public void setRegister__login_usecase(Register__Login_UseCase register__login_usecase) {
        this.register__login_usecase = register__login_usecase;
    }
    public Proceed_to_Checkout_UseCase getProceed_to_checkout_usecase() {
        return proceed_to_checkout_usecase;
    }

    public void setProceed_to_checkout_usecase(Proceed_to_Checkout_UseCase proceed_to_checkout_usecase) {
        this.proceed_to_checkout_usecase = proceed_to_checkout_usecase;
    }
    public Review_Order_UseCase getReview_order_usecase() {
        return review_order_usecase;
    }

    public void setReview_order_usecase(Review_Order_UseCase review_order_usecase) {
        this.review_order_usecase = review_order_usecase;
    }
    public Make_Payment___Checkout_UseCase getMake_payment___checkout_usecase() {
        return make_payment___checkout_usecase;
    }

    public void setMake_payment___checkout_usecase(Make_Payment___Checkout_UseCase make_payment___checkout_usecase) {
        this.make_payment___checkout_usecase = make_payment___checkout_usecase;
    }
    public Choose_Flight_UseCase getChoose_flight_usecase() {
        return choose_flight_usecase;
    }

    public void setChoose_flight_usecase(Choose_Flight_UseCase choose_flight_usecase) {
        this.choose_flight_usecase = choose_flight_usecase;
    }
    public Check_Tickets_UseCase getCheck_tickets_usecase() {
        return check_tickets_usecase;
    }

    public void setCheck_tickets_usecase(Check_Tickets_UseCase check_tickets_usecase) {
        this.check_tickets_usecase = check_tickets_usecase;
    }

}