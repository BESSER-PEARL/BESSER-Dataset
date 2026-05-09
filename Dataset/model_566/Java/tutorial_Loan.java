




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class tutorial_Loan  {

    private LocalDate date;





    private tutorial_Library tutorial_library;




    private tutorial_Book tutorial_book;




    private tutorial_Book tutorial_book;


    public tutorial_Loan(
        LocalDate date    ) {
        this.date = date;
    }


    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }

    public tutorial_Library getTutorial_library() {
        return tutorial_library;
    }

    public void setTutorial_library(tutorial_Library tutorial_library) {
        this.tutorial_library = tutorial_library;
    }
    public tutorial_Book getTutorial_book() {
        return tutorial_book;
    }

    public void setTutorial_book(tutorial_Book tutorial_book) {
        this.tutorial_book = tutorial_book;
    }
    public tutorial_Book getTutorial_book() {
        return tutorial_book;
    }

    public void setTutorial_book(tutorial_Book tutorial_book) {
        this.tutorial_book = tutorial_book;
    }

}