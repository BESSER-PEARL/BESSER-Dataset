





import java.util.List;
import java.util.ArrayList;

public class test_Person  {

    private String firstame;
    private String lastname;
    private String Grade;





    private test_Person test_person;




    private test_University test_university;




    private List<test_Person> test_persons;


    public test_Person(
        String firstame,        String lastname,        String Grade    ) {
        this.firstame = firstame;
        this.lastname = lastname;
        this.Grade = Grade;
        this.test_persons = new ArrayList<>();
    }

    public test_Person(
        String firstame,        String lastname,        String Grade        ArrayList<test_Person> test_persons    ) {
        this.firstame = firstame;
        this.lastname = lastname;
        this.Grade = Grade;
        this.test_persons = test_persons;
    }

    public String getFirstame() {
        return firstame;
    }

    public void setFirstame(String firstame) {
        this.firstame = firstame;
    }
    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }
    public String getGrade() {
        return Grade;
    }

    public void setGrade(String Grade) {
        this.Grade = Grade;
    }

    public test_Person getTest_person() {
        return test_person;
    }

    public void setTest_person(test_Person test_person) {
        this.test_person = test_person;
    }
    public test_University getTest_university() {
        return test_university;
    }

    public void setTest_university(test_University test_university) {
        this.test_university = test_university;
    }
    public List<test_Person> getTest_persons() {
        return test_persons;
    }

    public void addTest_person(Test_person test_person) {
        this.test_persons.add(test_person);
    }

}