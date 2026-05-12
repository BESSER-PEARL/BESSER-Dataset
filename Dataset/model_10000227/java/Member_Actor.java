





import java.util.List;
import java.util.ArrayList;

public class Member_Actor  {






    private Search_books_external search_books_external;




    private Cancel_membership_external cancel_membership_external;


    public Member_Actor(
    ) {
    }



    public Search_books_external getSearch_books_external() {
        return search_books_external;
    }

    public void setSearch_books_external(Search_books_external search_books_external) {
        this.search_books_external = search_books_external;
    }
    public Cancel_membership_external getCancel_membership_external() {
        return cancel_membership_external;
    }

    public void setCancel_membership_external(Cancel_membership_external cancel_membership_external) {
        this.cancel_membership_external = cancel_membership_external;
    }

}