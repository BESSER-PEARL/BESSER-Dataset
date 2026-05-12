





import java.util.List;
import java.util.ArrayList;

public class Librarian_Actor  {






    private Update_member_profile_external update_member_profile_external;




    private Return_book_external return_book_external;




    private Issue_book_external issue_book_external;


    public Librarian_Actor(
    ) {
    }



    public Update_member_profile_external getUpdate_member_profile_external() {
        return update_member_profile_external;
    }

    public void setUpdate_member_profile_external(Update_member_profile_external update_member_profile_external) {
        this.update_member_profile_external = update_member_profile_external;
    }
    public Return_book_external getReturn_book_external() {
        return return_book_external;
    }

    public void setReturn_book_external(Return_book_external return_book_external) {
        this.return_book_external = return_book_external;
    }
    public Issue_book_external getIssue_book_external() {
        return issue_book_external;
    }

    public void setIssue_book_external(Issue_book_external issue_book_external) {
        this.issue_book_external = issue_book_external;
    }

}