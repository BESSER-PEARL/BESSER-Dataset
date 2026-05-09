




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class ocltutorial_Loans  {

    private LocalDate date;





    private ocltutorial_Book ocltutorial_book;




    private ocltutorial_Library ocltutorial_library;




    private ocltutorial_Member ocltutorial_member;


    public ocltutorial_Loans(
        LocalDate date    ) {
        this.date = date;
    }


    public LocalDate getDate() {
        return date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }

    public ocltutorial_Book getOcltutorial_book() {
        return ocltutorial_book;
    }

    public void setOcltutorial_book(ocltutorial_Book ocltutorial_book) {
        this.ocltutorial_book = ocltutorial_book;
    }
    public ocltutorial_Library getOcltutorial_library() {
        return ocltutorial_library;
    }

    public void setOcltutorial_library(ocltutorial_Library ocltutorial_library) {
        this.ocltutorial_library = ocltutorial_library;
    }
    public ocltutorial_Member getOcltutorial_member() {
        return ocltutorial_member;
    }

    public void setOcltutorial_member(ocltutorial_Member ocltutorial_member) {
        this.ocltutorial_member = ocltutorial_member;
    }

}