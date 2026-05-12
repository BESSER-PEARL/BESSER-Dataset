





import java.util.List;
import java.util.ArrayList;

public class Book_Airline_Ticket_UseCase  {






    private User_Kaktus_Actor user_kaktus_actor;




    private Payment_UseCase payment_usecase;


    public Book_Airline_Ticket_UseCase(
    ) {
    }



    public User_Kaktus_Actor getUser_kaktus_actor() {
        return user_kaktus_actor;
    }

    public void setUser_kaktus_actor(User_Kaktus_Actor user_kaktus_actor) {
        this.user_kaktus_actor = user_kaktus_actor;
    }
    public Payment_UseCase getPayment_usecase() {
        return payment_usecase;
    }

    public void setPayment_usecase(Payment_UseCase payment_usecase) {
        this.payment_usecase = payment_usecase;
    }

}