





import java.util.List;
import java.util.ArrayList;

public class Railway_website_Actor  {






    private Fill_the_details_UseCase fill_the_details_usecase;




    private Pay_fare_amount_UseCase pay_fare_amount_usecase;




    private Book_ticket_UseCase book_ticket_usecase;




    private Refund_money_UseCase refund_money_usecase;




    private Cancel_ticket_UseCase cancel_ticket_usecase;


    public Railway_website_Actor(
    ) {
    }



    public Fill_the_details_UseCase getFill_the_details_usecase() {
        return fill_the_details_usecase;
    }

    public void setFill_the_details_usecase(Fill_the_details_UseCase fill_the_details_usecase) {
        this.fill_the_details_usecase = fill_the_details_usecase;
    }
    public Pay_fare_amount_UseCase getPay_fare_amount_usecase() {
        return pay_fare_amount_usecase;
    }

    public void setPay_fare_amount_usecase(Pay_fare_amount_UseCase pay_fare_amount_usecase) {
        this.pay_fare_amount_usecase = pay_fare_amount_usecase;
    }
    public Book_ticket_UseCase getBook_ticket_usecase() {
        return book_ticket_usecase;
    }

    public void setBook_ticket_usecase(Book_ticket_UseCase book_ticket_usecase) {
        this.book_ticket_usecase = book_ticket_usecase;
    }
    public Refund_money_UseCase getRefund_money_usecase() {
        return refund_money_usecase;
    }

    public void setRefund_money_usecase(Refund_money_UseCase refund_money_usecase) {
        this.refund_money_usecase = refund_money_usecase;
    }
    public Cancel_ticket_UseCase getCancel_ticket_usecase() {
        return cancel_ticket_usecase;
    }

    public void setCancel_ticket_usecase(Cancel_ticket_UseCase cancel_ticket_usecase) {
        this.cancel_ticket_usecase = cancel_ticket_usecase;
    }

}