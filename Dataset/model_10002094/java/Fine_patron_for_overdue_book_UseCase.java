





import java.util.List;
import java.util.ArrayList;

public class Fine_patron_for_overdue_book_UseCase  {






    private Library_Actor library_actor;




    private Pay_overdue_fine_UseCase pay_overdue_fine_usecase;


    public Fine_patron_for_overdue_book_UseCase(
    ) {
    }



    public Library_Actor getLibrary_actor() {
        return library_actor;
    }

    public void setLibrary_actor(Library_Actor library_actor) {
        this.library_actor = library_actor;
    }
    public Pay_overdue_fine_UseCase getPay_overdue_fine_usecase() {
        return pay_overdue_fine_usecase;
    }

    public void setPay_overdue_fine_usecase(Pay_overdue_fine_UseCase pay_overdue_fine_usecase) {
        this.pay_overdue_fine_usecase = pay_overdue_fine_usecase;
    }

}