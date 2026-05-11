





import java.util.List;
import java.util.ArrayList;

public class ramRoot_MTpos__Classroom extends MTpos__Element {

    private String id;





    private List<ramRoot_MTpos__Person> ramroot_mtpos__persons;




    private ramRoot_MTpos__Person ramroot_mtpos__person;


    public ramRoot_MTpos__Classroom(
        String id    ) {
        super(
        );
        this.id = id;
        this.ramroot_mtpos__persons = new ArrayList<>();
    }

    public ramRoot_MTpos__Classroom(
        String id        ArrayList<ramRoot_MTpos__Person> ramroot_mtpos__persons    ) {
        this.id = id;
        this.ramroot_mtpos__persons = ramroot_mtpos__persons;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<ramRoot_MTpos__Person> getRamroot_mtpos__persons() {
        return ramroot_mtpos__persons;
    }

    public void addRamroot_mtpos__person(Ramroot_mtpos__person ramroot_mtpos__person) {
        this.ramroot_mtpos__persons.add(ramroot_mtpos__person);
    }
    public ramRoot_MTpos__Person getRamroot_mtpos__person() {
        return ramroot_mtpos__person;
    }

    public void setRamroot_mtpos__person(ramRoot_MTpos__Person ramroot_mtpos__person) {
        this.ramroot_mtpos__person = ramroot_mtpos__person;
    }

}