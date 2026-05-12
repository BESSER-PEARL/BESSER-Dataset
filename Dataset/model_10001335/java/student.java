





import java.util.List;
import java.util.ArrayList;

public class student  {

    private String details;





    private books_database books_database;


    public student(
        String details    ) {
        this.details = details;
    }


    public String getDetails() {
        return details;
    }

    public void setDetails(String details) {
        this.details = details;
    }

    public books_database getBooks_database() {
        return books_database;
    }

    public void setBooks_database(books_database books_database) {
        this.books_database = books_database;
    }

}