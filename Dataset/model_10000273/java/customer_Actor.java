





import java.util.List;
import java.util.ArrayList;

public class customer_Actor  {






    private confirm_purchase_UseCase confirm_purchase_usecase;




    private search_flights_UseCase search_flights_usecase;




    private round_trip_or_one_way__UseCase round_trip_or_one_way__usecase;




    private enter_date_UseCase enter_date_usecase;




    private select_flight_UseCase select_flight_usecase;




    private print_ticket_UseCase print_ticket_usecase;




    private enter_airport_UseCase1 enter_airport_usecase1;




    private make_payment_UseCase make_payment_usecase;




    private enter_no__of_tickets_UseCase enter_no__of_tickets_usecase;


    public customer_Actor(
    ) {
    }



    public confirm_purchase_UseCase getConfirm_purchase_usecase() {
        return confirm_purchase_usecase;
    }

    public void setConfirm_purchase_usecase(confirm_purchase_UseCase confirm_purchase_usecase) {
        this.confirm_purchase_usecase = confirm_purchase_usecase;
    }
    public search_flights_UseCase getSearch_flights_usecase() {
        return search_flights_usecase;
    }

    public void setSearch_flights_usecase(search_flights_UseCase search_flights_usecase) {
        this.search_flights_usecase = search_flights_usecase;
    }
    public round_trip_or_one_way__UseCase getRound_trip_or_one_way__usecase() {
        return round_trip_or_one_way__usecase;
    }

    public void setRound_trip_or_one_way__usecase(round_trip_or_one_way__UseCase round_trip_or_one_way__usecase) {
        this.round_trip_or_one_way__usecase = round_trip_or_one_way__usecase;
    }
    public enter_date_UseCase getEnter_date_usecase() {
        return enter_date_usecase;
    }

    public void setEnter_date_usecase(enter_date_UseCase enter_date_usecase) {
        this.enter_date_usecase = enter_date_usecase;
    }
    public select_flight_UseCase getSelect_flight_usecase() {
        return select_flight_usecase;
    }

    public void setSelect_flight_usecase(select_flight_UseCase select_flight_usecase) {
        this.select_flight_usecase = select_flight_usecase;
    }
    public print_ticket_UseCase getPrint_ticket_usecase() {
        return print_ticket_usecase;
    }

    public void setPrint_ticket_usecase(print_ticket_UseCase print_ticket_usecase) {
        this.print_ticket_usecase = print_ticket_usecase;
    }
    public enter_airport_UseCase1 getEnter_airport_usecase1() {
        return enter_airport_usecase1;
    }

    public void setEnter_airport_usecase1(enter_airport_UseCase1 enter_airport_usecase1) {
        this.enter_airport_usecase1 = enter_airport_usecase1;
    }
    public make_payment_UseCase getMake_payment_usecase() {
        return make_payment_usecase;
    }

    public void setMake_payment_usecase(make_payment_UseCase make_payment_usecase) {
        this.make_payment_usecase = make_payment_usecase;
    }
    public enter_no__of_tickets_UseCase getEnter_no__of_tickets_usecase() {
        return enter_no__of_tickets_usecase;
    }

    public void setEnter_no__of_tickets_usecase(enter_no__of_tickets_UseCase enter_no__of_tickets_usecase) {
        this.enter_no__of_tickets_usecase = enter_no__of_tickets_usecase;
    }

}