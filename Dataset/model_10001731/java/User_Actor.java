





import java.util.List;
import java.util.ArrayList;

public class User_Actor  {






    private Borrow_Book_UseCase borrow_book_usecase;




    private View_Books_UseCase view_books_usecase;


    public User_Actor(
    ) {
    }



    public Borrow_Book_UseCase getBorrow_book_usecase() {
        return borrow_book_usecase;
    }

    public void setBorrow_book_usecase(Borrow_Book_UseCase borrow_book_usecase) {
        this.borrow_book_usecase = borrow_book_usecase;
    }
    public View_Books_UseCase getView_books_usecase() {
        return view_books_usecase;
    }

    public void setView_books_usecase(View_Books_UseCase view_books_usecase) {
        this.view_books_usecase = view_books_usecase;
    }

}