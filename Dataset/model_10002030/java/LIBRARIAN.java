





import java.util.List;
import java.util.ArrayList;

public class LIBRARIAN  {

    private String LIBRARIAN_ID;
    private String issue_status;
    private String searchbook__;
    private String issue_book;
    private String verify_member__;
    private String NAME;





    private library library;


    public LIBRARIAN(
        String LIBRARIAN_ID,        String issue_status,        String searchbook__,        String issue_book,        String verify_member__,        String NAME    ) {
        this.LIBRARIAN_ID = LIBRARIAN_ID;
        this.issue_status = issue_status;
        this.searchbook__ = searchbook__;
        this.issue_book = issue_book;
        this.verify_member__ = verify_member__;
        this.NAME = NAME;
    }


    public String getLibrarian_id() {
        return LIBRARIAN_ID;
    }

    public void setLibrarian_id(String LIBRARIAN_ID) {
        this.LIBRARIAN_ID = LIBRARIAN_ID;
    }
    public String getIssue_status() {
        return issue_status;
    }

    public void setIssue_status(String issue_status) {
        this.issue_status = issue_status;
    }
    public String getSearchbook__() {
        return searchbook__;
    }

    public void setSearchbook__(String searchbook__) {
        this.searchbook__ = searchbook__;
    }
    public String getIssue_book() {
        return issue_book;
    }

    public void setIssue_book(String issue_book) {
        this.issue_book = issue_book;
    }
    public String getVerify_member__() {
        return verify_member__;
    }

    public void setVerify_member__(String verify_member__) {
        this.verify_member__ = verify_member__;
    }
    public String getName() {
        return NAME;
    }

    public void setName(String NAME) {
        this.NAME = NAME;
    }

    public library getLibrary() {
        return library;
    }

    public void setLibrary(library library) {
        this.library = library;
    }

}