





import java.util.List;
import java.util.ArrayList;

public class Fine  {

    private int fine_amount;
    private int book_id;
    private int member_id;
    private String borrowed_date;
    private String returned_date;





    private List<Librarian> librarians;




    private Member member;


    public Fine(
        int fine_amount,        int book_id,        int member_id,        String borrowed_date,        String returned_date    ) {
        this.fine_amount = fine_amount;
        this.book_id = book_id;
        this.member_id = member_id;
        this.borrowed_date = borrowed_date;
        this.returned_date = returned_date;
        this.librarians = new ArrayList<>();
    }

    public Fine(
        int fine_amount,        int book_id,        int member_id,        String borrowed_date,        String returned_date        ArrayList<Librarian> librarians    ) {
        this.fine_amount = fine_amount;
        this.book_id = book_id;
        this.member_id = member_id;
        this.borrowed_date = borrowed_date;
        this.returned_date = returned_date;
        this.librarians = librarians;
    }

    public int getFine_amount() {
        return fine_amount;
    }

    public void setFine_amount(int fine_amount) {
        this.fine_amount = fine_amount;
    }
    public int getBook_id() {
        return book_id;
    }

    public void setBook_id(int book_id) {
        this.book_id = book_id;
    }
    public int getMember_id() {
        return member_id;
    }

    public void setMember_id(int member_id) {
        this.member_id = member_id;
    }
    public String getBorrowed_date() {
        return borrowed_date;
    }

    public void setBorrowed_date(String borrowed_date) {
        this.borrowed_date = borrowed_date;
    }
    public String getReturned_date() {
        return returned_date;
    }

    public void setReturned_date(String returned_date) {
        this.returned_date = returned_date;
    }

    public List<Librarian> getLibrarians() {
        return librarians;
    }

    public void addLibrarian(Librarian librarian) {
        this.librarians.add(librarian);
    }
    public Member getMember() {
        return member;
    }

    public void setMember(Member member) {
        this.member = member;
    }

}