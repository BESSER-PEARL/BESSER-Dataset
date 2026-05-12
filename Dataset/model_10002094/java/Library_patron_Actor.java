





import java.util.List;
import java.util.ArrayList;

public class Library_patron_Actor  {






    private Pay_overdue_fine_UseCase pay_overdue_fine_usecase;




    private Check_out_book_UseCase check_out_book_usecase;




    private Put_book_on_reserve_UseCase put_book_on_reserve_usecase;


    public Library_patron_Actor(
    ) {
    }



    public Pay_overdue_fine_UseCase getPay_overdue_fine_usecase() {
        return pay_overdue_fine_usecase;
    }

    public void setPay_overdue_fine_usecase(Pay_overdue_fine_UseCase pay_overdue_fine_usecase) {
        this.pay_overdue_fine_usecase = pay_overdue_fine_usecase;
    }
    public Check_out_book_UseCase getCheck_out_book_usecase() {
        return check_out_book_usecase;
    }

    public void setCheck_out_book_usecase(Check_out_book_UseCase check_out_book_usecase) {
        this.check_out_book_usecase = check_out_book_usecase;
    }
    public Put_book_on_reserve_UseCase getPut_book_on_reserve_usecase() {
        return put_book_on_reserve_usecase;
    }

    public void setPut_book_on_reserve_usecase(Put_book_on_reserve_UseCase put_book_on_reserve_usecase) {
        this.put_book_on_reserve_usecase = put_book_on_reserve_usecase;
    }

}