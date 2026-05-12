





import java.util.List;
import java.util.ArrayList;

public class Waiter_Actor  {






    private Input_payment_details_external input_payment_details_external;




    private Print_bill_external print_bill_external;




    private Alerted_to_Serve_Food_external alerted_to_serve_food_external;




    private Alerted_to_Serve_drinks_external alerted_to_serve_drinks_external;


    public Waiter_Actor(
    ) {
    }



    public Input_payment_details_external getInput_payment_details_external() {
        return input_payment_details_external;
    }

    public void setInput_payment_details_external(Input_payment_details_external input_payment_details_external) {
        this.input_payment_details_external = input_payment_details_external;
    }
    public Print_bill_external getPrint_bill_external() {
        return print_bill_external;
    }

    public void setPrint_bill_external(Print_bill_external print_bill_external) {
        this.print_bill_external = print_bill_external;
    }
    public Alerted_to_Serve_Food_external getAlerted_to_serve_food_external() {
        return alerted_to_serve_food_external;
    }

    public void setAlerted_to_serve_food_external(Alerted_to_Serve_Food_external alerted_to_serve_food_external) {
        this.alerted_to_serve_food_external = alerted_to_serve_food_external;
    }
    public Alerted_to_Serve_drinks_external getAlerted_to_serve_drinks_external() {
        return alerted_to_serve_drinks_external;
    }

    public void setAlerted_to_serve_drinks_external(Alerted_to_Serve_drinks_external alerted_to_serve_drinks_external) {
        this.alerted_to_serve_drinks_external = alerted_to_serve_drinks_external;
    }

}