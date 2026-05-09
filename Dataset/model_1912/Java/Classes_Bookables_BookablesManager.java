





import java.util.List;
import java.util.ArrayList;

public class Classes_Bookables_BookablesManager extends IBookablesManage {






    private List<Bookable> bookables;


    public Classes_Bookables_BookablesManager(
    ) {
        super(
        );
        this.bookables = new ArrayList<>();
    }

    public Classes_Bookables_BookablesManager(
        ArrayList<Bookable> bookables    ) {
        this.bookables = bookables;
    }


    public List<Bookable> getBookables() {
        return bookables;
    }

    public void addBookable(Bookable bookable) {
        this.bookables.add(bookable);
    }

}