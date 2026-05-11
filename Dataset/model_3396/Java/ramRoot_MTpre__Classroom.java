





import java.util.List;
import java.util.ArrayList;

public class ramRoot_MTpre__Classroom extends MTpre__Element {

    private String id;





    private ramRoot_MTpre__Person ramroot_mtpre__person;




    private List<ramRoot_MTpre__Person> ramroot_mtpre__persons;


    public ramRoot_MTpre__Classroom(
        String id    ) {
        super(
        );
        this.id = id;
        this.ramroot_mtpre__persons = new ArrayList<>();
    }

    public ramRoot_MTpre__Classroom(
        String id        ArrayList<ramRoot_MTpre__Person> ramroot_mtpre__persons    ) {
        this.id = id;
        this.ramroot_mtpre__persons = ramroot_mtpre__persons;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public ramRoot_MTpre__Person getRamroot_mtpre__person() {
        return ramroot_mtpre__person;
    }

    public void setRamroot_mtpre__person(ramRoot_MTpre__Person ramroot_mtpre__person) {
        this.ramroot_mtpre__person = ramroot_mtpre__person;
    }
    public List<ramRoot_MTpre__Person> getRamroot_mtpre__persons() {
        return ramroot_mtpre__persons;
    }

    public void addRamroot_mtpre__person(Ramroot_mtpre__person ramroot_mtpre__person) {
        this.ramroot_mtpre__persons.add(ramroot_mtpre__person);
    }

}