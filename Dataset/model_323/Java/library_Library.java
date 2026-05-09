





import java.util.List;
import java.util.ArrayList;

public class library_Library  {

    private String address;
    private String name;





    private List<library__cPfTBB9KEeeOINGRvT6ccg> library__cpftbb9keeeoingrvt6ccgs;




    private List<library__cPfTDx9KEeeOINGRvT6ccg> library__cpftdx9keeeoingrvt6ccgs;


    public library_Library(
        String address,        String name    ) {
        this.address = address;
        this.name = name;
        this.library__cpftbb9keeeoingrvt6ccgs = new ArrayList<>();
        this.library__cpftdx9keeeoingrvt6ccgs = new ArrayList<>();
    }

    public library_Library(
        String address,        String name        ArrayList<library__cPfTBB9KEeeOINGRvT6ccg> library__cpftbb9keeeoingrvt6ccgs,        ArrayList<library__cPfTDx9KEeeOINGRvT6ccg> library__cpftdx9keeeoingrvt6ccgs    ) {
        this.address = address;
        this.name = name;
        this.library__cpftbb9keeeoingrvt6ccgs = library__cpftbb9keeeoingrvt6ccgs;
        this.library__cpftdx9keeeoingrvt6ccgs = library__cpftdx9keeeoingrvt6ccgs;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<library__cPfTBB9KEeeOINGRvT6ccg> getLibrary__cpftbb9keeeoingrvt6ccgs() {
        return library__cpftbb9keeeoingrvt6ccgs;
    }

    public void addLibrary__cpftbb9keeeoingrvt6ccg(Library__cpftbb9keeeoingrvt6ccg library__cpftbb9keeeoingrvt6ccg) {
        this.library__cpftbb9keeeoingrvt6ccgs.add(library__cpftbb9keeeoingrvt6ccg);
    }
    public List<library__cPfTDx9KEeeOINGRvT6ccg> getLibrary__cpftdx9keeeoingrvt6ccgs() {
        return library__cpftdx9keeeoingrvt6ccgs;
    }

    public void addLibrary__cpftdx9keeeoingrvt6ccg(Library__cpftdx9keeeoingrvt6ccg library__cpftdx9keeeoingrvt6ccg) {
        this.library__cpftdx9keeeoingrvt6ccgs.add(library__cpftdx9keeeoingrvt6ccg);
    }

}