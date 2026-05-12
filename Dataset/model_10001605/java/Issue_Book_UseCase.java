





import java.util.List;
import java.util.ArrayList;

public class Issue_Book_UseCase  {






    private Checkout_Librarian_Actor checkout_librarian_actor;


    public Issue_Book_UseCase(
    ) {
    }



    public Checkout_Librarian_Actor getCheckout_librarian_actor() {
        return checkout_librarian_actor;
    }

    public void setCheckout_librarian_actor(Checkout_Librarian_Actor checkout_librarian_actor) {
        this.checkout_librarian_actor = checkout_librarian_actor;
    }

}