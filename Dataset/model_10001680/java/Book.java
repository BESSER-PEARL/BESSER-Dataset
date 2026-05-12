





import java.util.List;
import java.util.ArrayList;

public class Book  {

    private int Book_ISBN;
    private String book_name;
    private int Book_Author;



    public Book(
        int Book_ISBN,        String book_name,        int Book_Author    ) {
        this.Book_ISBN = Book_ISBN;
        this.book_name = book_name;
        this.Book_Author = Book_Author;
    }


    public int getBook_isbn() {
        return Book_ISBN;
    }

    public void setBook_isbn(int Book_ISBN) {
        this.Book_ISBN = Book_ISBN;
    }
    public String getBook_name() {
        return book_name;
    }

    public void setBook_name(String book_name) {
        this.book_name = book_name;
    }
    public int getBook_author() {
        return Book_Author;
    }

    public void setBook_author(int Book_Author) {
        this.Book_Author = Book_Author;
    }


}