





import java.util.List;
import java.util.ArrayList;

public class Hospital  {

    private String name;
    private int phone;
    private String address;





    private List<Person> persons;




    private List<Person> persons;




    private Person person;


    public Hospital(
        String name,        int phone,        String address    ) {
        this.name = name;
        this.phone = phone;
        this.address = address;
        this.persons = new ArrayList<>();
        this.persons = new ArrayList<>();
    }

    public Hospital(
        String name,        int phone,        String address        ArrayList<Person> persons,        ArrayList<Person> persons    ) {
        this.name = name;
        this.phone = phone;
        this.address = address;
        this.persons = persons;
        this.persons = persons;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getPhone() {
        return phone;
    }

    public void setPhone(int phone) {
        this.phone = phone;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public List<Person> getPersons() {
        return persons;
    }

    public void addPerson(Person person) {
        this.persons.add(person);
    }
    public List<Person> getPersons() {
        return persons;
    }

    public void addPerson(Person person) {
        this.persons.add(person);
    }
    public Person getPerson() {
        return person;
    }

    public void setPerson(Person person) {
        this.person = person;
    }

}