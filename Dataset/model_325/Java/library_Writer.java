





import java.util.List;
import java.util.ArrayList;

public class library_Writer  {

    private String name;





    private List<library__cPfTDx9KEeeOINGRvT6ccg> library__cpftdx9keeeoingrvt6ccgs;


    public library_Writer(
        String name    ) {
        this.name = name;
        this.library__cpftdx9keeeoingrvt6ccgs = new ArrayList<>();
    }

    public library_Writer(
        String name        ArrayList<library__cPfTDx9KEeeOINGRvT6ccg> library__cpftdx9keeeoingrvt6ccgs    ) {
        this.name = name;
        this.library__cpftdx9keeeoingrvt6ccgs = library__cpftdx9keeeoingrvt6ccgs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<library__cPfTDx9KEeeOINGRvT6ccg> getLibrary__cpftdx9keeeoingrvt6ccgs() {
        return library__cpftdx9keeeoingrvt6ccgs;
    }

    public void addLibrary__cpftdx9keeeoingrvt6ccg(Library__cpftdx9keeeoingrvt6ccg library__cpftdx9keeeoingrvt6ccg) {
        this.library__cpftdx9keeeoingrvt6ccgs.add(library__cpftdx9keeeoingrvt6ccg);
    }

}