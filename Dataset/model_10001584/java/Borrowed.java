





import java.util.List;
import java.util.ArrayList;

public class Borrowed  {

    private String borrowed_date;
    private String returned_date;





    private List<Books> bookss;




    private List<Member> members;


    public Borrowed(
        String borrowed_date,        String returned_date    ) {
        this.borrowed_date = borrowed_date;
        this.returned_date = returned_date;
        this.bookss = new ArrayList<>();
        this.members = new ArrayList<>();
    }

    public Borrowed(
        String borrowed_date,        String returned_date        ArrayList<Books> bookss,        ArrayList<Member> members    ) {
        this.borrowed_date = borrowed_date;
        this.returned_date = returned_date;
        this.bookss = bookss;
        this.members = members;
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

    public List<Books> getBookss() {
        return bookss;
    }

    public void addBooks(Books books) {
        this.bookss.add(books);
    }
    public List<Member> getMembers() {
        return members;
    }

    public void addMember(Member member) {
        this.members.add(member);
    }

}