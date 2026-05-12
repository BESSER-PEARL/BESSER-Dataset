





import java.util.List;
import java.util.ArrayList;

public class Payment_UseCase  {






    private Book_Airline_Ticket_UseCase book_airline_ticket_usecase;


    public Payment_UseCase(
    ) {
    }



    public Book_Airline_Ticket_UseCase getBook_airline_ticket_usecase() {
        return book_airline_ticket_usecase;
    }

    public void setBook_airline_ticket_usecase(Book_Airline_Ticket_UseCase book_airline_ticket_usecase) {
        this.book_airline_ticket_usecase = book_airline_ticket_usecase;
    }

}