





import java.util.List;
import java.util.ArrayList;

public class mm1_Library  {

    private String name;





    private List<mm1_Book> mm1_books;




    private List<mm1_Member> mm1_members;




    private List<mm1_Film> mm1_films;


    public mm1_Library(
        String name    ) {
        this.name = name;
        this.mm1_books = new ArrayList<>();
        this.mm1_members = new ArrayList<>();
        this.mm1_films = new ArrayList<>();
    }

    public mm1_Library(
        String name        ArrayList<mm1_Book> mm1_books,        ArrayList<mm1_Member> mm1_members,        ArrayList<mm1_Film> mm1_films    ) {
        this.name = name;
        this.mm1_books = mm1_books;
        this.mm1_members = mm1_members;
        this.mm1_films = mm1_films;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<mm1_Book> getMm1_books() {
        return mm1_books;
    }

    public void addMm1_book(Mm1_book mm1_book) {
        this.mm1_books.add(mm1_book);
    }
    public List<mm1_Member> getMm1_members() {
        return mm1_members;
    }

    public void addMm1_member(Mm1_member mm1_member) {
        this.mm1_members.add(mm1_member);
    }
    public List<mm1_Film> getMm1_films() {
        return mm1_films;
    }

    public void addMm1_film(Mm1_film mm1_film) {
        this.mm1_films.add(mm1_film);
    }

}