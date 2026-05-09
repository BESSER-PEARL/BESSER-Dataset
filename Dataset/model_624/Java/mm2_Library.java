





import java.util.List;
import java.util.ArrayList;

public class mm2_Library  {

    private String name;





    private List<mm2_Member> mm2_members;




    private List<mm2_Loan> mm2_loans;




    private List<mm2_Book> mm2_books;


    public mm2_Library(
        String name    ) {
        this.name = name;
        this.mm2_members = new ArrayList<>();
        this.mm2_loans = new ArrayList<>();
        this.mm2_books = new ArrayList<>();
    }

    public mm2_Library(
        String name        ArrayList<mm2_Member> mm2_members,        ArrayList<mm2_Loan> mm2_loans,        ArrayList<mm2_Book> mm2_books    ) {
        this.name = name;
        this.mm2_members = mm2_members;
        this.mm2_loans = mm2_loans;
        this.mm2_books = mm2_books;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<mm2_Member> getMm2_members() {
        return mm2_members;
    }

    public void addMm2_member(Mm2_member mm2_member) {
        this.mm2_members.add(mm2_member);
    }
    public List<mm2_Loan> getMm2_loans() {
        return mm2_loans;
    }

    public void addMm2_loan(Mm2_loan mm2_loan) {
        this.mm2_loans.add(mm2_loan);
    }
    public List<mm2_Book> getMm2_books() {
        return mm2_books;
    }

    public void addMm2_book(Mm2_book mm2_book) {
        this.mm2_books.add(mm2_book);
    }

}