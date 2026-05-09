





import java.util.List;
import java.util.ArrayList;

public class sistedesMM_Publication  {






    private List<sistedesMM_Person> sistedesmm_persons;




    private sistedesMM_Person sistedesmm_person;


    public sistedesMM_Publication(
    ) {
        this.sistedesmm_persons = new ArrayList<>();
    }

    public sistedesMM_Publication(
        ArrayList<sistedesMM_Person> sistedesmm_persons    ) {
        this.sistedesmm_persons = sistedesmm_persons;
    }


    public List<sistedesMM_Person> getSistedesmm_persons() {
        return sistedesmm_persons;
    }

    public void addSistedesmm_person(Sistedesmm_person sistedesmm_person) {
        this.sistedesmm_persons.add(sistedesmm_person);
    }
    public sistedesMM_Person getSistedesmm_person() {
        return sistedesmm_person;
    }

    public void setSistedesmm_person(sistedesMM_Person sistedesmm_person) {
        this.sistedesmm_person = sistedesmm_person;
    }

}