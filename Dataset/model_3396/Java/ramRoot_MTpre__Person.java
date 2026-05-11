





import java.util.List;
import java.util.ArrayList;

public class ramRoot_MTpre__Person extends MTpre__Element {

    private String name;





    private List<ramRoot_MTpre__Person> ramroot_mtpre__persons;


    public ramRoot_MTpre__Person(
        String name    ) {
        super(
        );
        this.name = name;
        this.ramroot_mtpre__persons = new ArrayList<>();
    }

    public ramRoot_MTpre__Person(
        String name        ArrayList<ramRoot_MTpre__Person> ramroot_mtpre__persons    ) {
        this.name = name;
        this.ramroot_mtpre__persons = ramroot_mtpre__persons;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<ramRoot_MTpre__Person> getRamroot_mtpre__persons() {
        return ramroot_mtpre__persons;
    }

    public void addRamroot_mtpre__person(Ramroot_mtpre__person ramroot_mtpre__person) {
        this.ramroot_mtpre__persons.add(ramroot_mtpre__person);
    }

}