





import java.util.List;
import java.util.ArrayList;

public class Librarian_Actor  {






    private Issue_member_card_external issue_member_card_external;




    private Issue_book_external issue_book_external;




    private Maintain_book_in_records_external maintain_book_in_records_external;




    private Return_book_external return_book_external;




    private Update_member_profile_external update_member_profile_external;


    public Librarian_Actor(
    ) {
    }



    public Issue_member_card_external getIssue_member_card_external() {
        return issue_member_card_external;
    }

    public void setIssue_member_card_external(Issue_member_card_external issue_member_card_external) {
        this.issue_member_card_external = issue_member_card_external;
    }
    public Issue_book_external getIssue_book_external() {
        return issue_book_external;
    }

    public void setIssue_book_external(Issue_book_external issue_book_external) {
        this.issue_book_external = issue_book_external;
    }
    public Maintain_book_in_records_external getMaintain_book_in_records_external() {
        return maintain_book_in_records_external;
    }

    public void setMaintain_book_in_records_external(Maintain_book_in_records_external maintain_book_in_records_external) {
        this.maintain_book_in_records_external = maintain_book_in_records_external;
    }
    public Return_book_external getReturn_book_external() {
        return return_book_external;
    }

    public void setReturn_book_external(Return_book_external return_book_external) {
        this.return_book_external = return_book_external;
    }
    public Update_member_profile_external getUpdate_member_profile_external() {
        return update_member_profile_external;
    }

    public void setUpdate_member_profile_external(Update_member_profile_external update_member_profile_external) {
        this.update_member_profile_external = update_member_profile_external;
    }

}