





import java.util.List;
import java.util.ArrayList;

public class emftest_Library  {






    private List<emftest_BookCollection> emftest_bookcollections;


    public emftest_Library(
    ) {
        this.emftest_bookcollections = new ArrayList<>();
    }

    public emftest_Library(
        ArrayList<emftest_BookCollection> emftest_bookcollections    ) {
        this.emftest_bookcollections = emftest_bookcollections;
    }


    public List<emftest_BookCollection> getEmftest_bookcollections() {
        return emftest_bookcollections;
    }

    public void addEmftest_bookcollection(Emftest_bookcollection emftest_bookcollection) {
        this.emftest_bookcollections.add(emftest_bookcollection);
    }

}