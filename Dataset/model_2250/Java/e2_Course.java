





import java.util.List;
import java.util.ArrayList;

public class e2_Course  {

    private String ID;
    private String Name;
    private float Credit;





    private List<e2_Person> e2_persons;




    private List<e2_Assingnment> e2_assingnments;




    private List<e2_Person> e2_persons;




    private List<e2_Person> e2_persons;


    public e2_Course(
        String ID,        String Name,        float Credit    ) {
        this.ID = ID;
        this.Name = Name;
        this.Credit = Credit;
        this.e2_persons = new ArrayList<>();
        this.e2_assingnments = new ArrayList<>();
        this.e2_persons = new ArrayList<>();
        this.e2_persons = new ArrayList<>();
    }

    public e2_Course(
        String ID,        String Name,        float Credit        ArrayList<e2_Person> e2_persons,        ArrayList<e2_Assingnment> e2_assingnments,        ArrayList<e2_Person> e2_persons,        ArrayList<e2_Person> e2_persons    ) {
        this.ID = ID;
        this.Name = Name;
        this.Credit = Credit;
        this.e2_persons = e2_persons;
        this.e2_assingnments = e2_assingnments;
        this.e2_persons = e2_persons;
        this.e2_persons = e2_persons;
    }

    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public float getCredit() {
        return Credit;
    }

    public void setCredit(float Credit) {
        this.Credit = Credit;
    }

    public List<e2_Person> getE2_persons() {
        return e2_persons;
    }

    public void addE2_person(E2_person e2_person) {
        this.e2_persons.add(e2_person);
    }
    public List<e2_Assingnment> getE2_assingnments() {
        return e2_assingnments;
    }

    public void addE2_assingnment(E2_assingnment e2_assingnment) {
        this.e2_assingnments.add(e2_assingnment);
    }
    public List<e2_Person> getE2_persons() {
        return e2_persons;
    }

    public void addE2_person(E2_person e2_person) {
        this.e2_persons.add(e2_person);
    }
    public List<e2_Person> getE2_persons() {
        return e2_persons;
    }

    public void addE2_person(E2_person e2_person) {
        this.e2_persons.add(e2_person);
    }

}