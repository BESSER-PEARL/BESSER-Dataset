





import java.util.List;
import java.util.ArrayList;

public class lazy_Library  {

    private String name;





    private List<lazy_Writer> lazy_writers;


    public lazy_Library(
        String name    ) {
        this.name = name;
        this.lazy_writers = new ArrayList<>();
    }

    public lazy_Library(
        String name        ArrayList<lazy_Writer> lazy_writers    ) {
        this.name = name;
        this.lazy_writers = lazy_writers;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<lazy_Writer> getLazy_writers() {
        return lazy_writers;
    }

    public void addLazy_writer(Lazy_writer lazy_writer) {
        this.lazy_writers.add(lazy_writer);
    }

}