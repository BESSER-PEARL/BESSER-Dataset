





import java.util.List;
import java.util.ArrayList;

public class ramRoot_MTpos__Person extends MTpos__Element {

    private String name;





    private List<ramRoot_MTpos__Person> ramroot_mtpos__persons;


    public ramRoot_MTpos__Person(
        String name    ) {
        super(
        );
        this.name = name;
        this.ramroot_mtpos__persons = new ArrayList<>();
    }

    public ramRoot_MTpos__Person(
        String name        ArrayList<ramRoot_MTpos__Person> ramroot_mtpos__persons    ) {
        this.name = name;
        this.ramroot_mtpos__persons = ramroot_mtpos__persons;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<ramRoot_MTpos__Person> getRamroot_mtpos__persons() {
        return ramroot_mtpos__persons;
    }

    public void addRamroot_mtpos__person(Ramroot_mtpos__person ramroot_mtpos__person) {
        this.ramroot_mtpos__persons.add(ramroot_mtpos__person);
    }

}