





import java.util.List;
import java.util.ArrayList;

public class Faculty_Actor  {






    private Reserve_Book_For_Semester_external reserve_book_for_semester_external;




    private Extended_Checkout_external extended_checkout_external;


    public Faculty_Actor(
    ) {
    }



    public Reserve_Book_For_Semester_external getReserve_book_for_semester_external() {
        return reserve_book_for_semester_external;
    }

    public void setReserve_book_for_semester_external(Reserve_Book_For_Semester_external reserve_book_for_semester_external) {
        this.reserve_book_for_semester_external = reserve_book_for_semester_external;
    }
    public Extended_Checkout_external getExtended_checkout_external() {
        return extended_checkout_external;
    }

    public void setExtended_checkout_external(Extended_Checkout_external extended_checkout_external) {
        this.extended_checkout_external = extended_checkout_external;
    }

}