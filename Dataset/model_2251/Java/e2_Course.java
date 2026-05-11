





import java.util.List;
import java.util.ArrayList;

public class e2_Course  {

    private String Name;
    private String ID;
    private float Credit;





    private List<e2_Person> e2_persons;




    private List<e2_Person> e2_persons;




    private List<e2_Person> e2_persons;




    private List<e2_Assingnment> e2_assingnments;




    private List<e2_Lecture> e2_lectures;




    private List<e2_Group> e2_groups;


    public e2_Course(
        String Name,        String ID,        float Credit    ) {
        this.Name = Name;
        this.ID = ID;
        this.Credit = Credit;
        this.e2_persons = new ArrayList<>();
        this.e2_persons = new ArrayList<>();
        this.e2_persons = new ArrayList<>();
        this.e2_assingnments = new ArrayList<>();
        this.e2_lectures = new ArrayList<>();
        this.e2_groups = new ArrayList<>();
    }

    public e2_Course(
        String Name,        String ID,        float Credit        ArrayList<e2_Person> e2_persons,        ArrayList<e2_Person> e2_persons,        ArrayList<e2_Person> e2_persons,        ArrayList<e2_Assingnment> e2_assingnments,        ArrayList<e2_Lecture> e2_lectures,        ArrayList<e2_Group> e2_groups    ) {
        this.Name = Name;
        this.ID = ID;
        this.Credit = Credit;
        this.e2_persons = e2_persons;
        this.e2_persons = e2_persons;
        this.e2_persons = e2_persons;
        this.e2_assingnments = e2_assingnments;
        this.e2_lectures = e2_lectures;
        this.e2_groups = e2_groups;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
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
    public List<e2_Assingnment> getE2_assingnments() {
        return e2_assingnments;
    }

    public void addE2_assingnment(E2_assingnment e2_assingnment) {
        this.e2_assingnments.add(e2_assingnment);
    }
    public List<e2_Lecture> getE2_lectures() {
        return e2_lectures;
    }

    public void addE2_lecture(E2_lecture e2_lecture) {
        this.e2_lectures.add(e2_lecture);
    }
    public List<e2_Group> getE2_groups() {
        return e2_groups;
    }

    public void addE2_group(E2_group e2_group) {
        this.e2_groups.add(e2_group);
    }

}