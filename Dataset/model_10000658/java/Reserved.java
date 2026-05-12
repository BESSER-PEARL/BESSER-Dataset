





import java.util.List;
import java.util.ArrayList;

public class Reserved  {

    private String reserved_date;





    private List<Member> members;




    private List<Books> bookss;


    public Reserved(
        String reserved_date    ) {
        this.reserved_date = reserved_date;
        this.members = new ArrayList<>();
        this.bookss = new ArrayList<>();
    }

    public Reserved(
        String reserved_date        ArrayList<Member> members,        ArrayList<Books> bookss    ) {
        this.reserved_date = reserved_date;
        this.members = members;
        this.bookss = bookss;
    }

    public String getReserved_date() {
        return reserved_date;
    }

    public void setReserved_date(String reserved_date) {
        this.reserved_date = reserved_date;
    }

    public List<Member> getMembers() {
        return members;
    }

    public void addMember(Member member) {
        this.members.add(member);
    }
    public List<Books> getBookss() {
        return bookss;
    }

    public void addBooks(Books books) {
        this.bookss.add(books);
    }

}