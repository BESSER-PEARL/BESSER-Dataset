





import java.util.List;
import java.util.ArrayList;

public class Patron_Actor  {






    private Checkout_book_UseCase checkout_book_usecase;




    private Return_book_UseCase return_book_usecase;




    private Create_library_account_UseCase create_library_account_usecase;




    private Request_Book_UseCase request_book_usecase;


    public Patron_Actor(
    ) {
    }



    public Checkout_book_UseCase getCheckout_book_usecase() {
        return checkout_book_usecase;
    }

    public void setCheckout_book_usecase(Checkout_book_UseCase checkout_book_usecase) {
        this.checkout_book_usecase = checkout_book_usecase;
    }
    public Return_book_UseCase getReturn_book_usecase() {
        return return_book_usecase;
    }

    public void setReturn_book_usecase(Return_book_UseCase return_book_usecase) {
        this.return_book_usecase = return_book_usecase;
    }
    public Create_library_account_UseCase getCreate_library_account_usecase() {
        return create_library_account_usecase;
    }

    public void setCreate_library_account_usecase(Create_library_account_UseCase create_library_account_usecase) {
        this.create_library_account_usecase = create_library_account_usecase;
    }
    public Request_Book_UseCase getRequest_book_usecase() {
        return request_book_usecase;
    }

    public void setRequest_book_usecase(Request_Book_UseCase request_book_usecase) {
        this.request_book_usecase = request_book_usecase;
    }

}