





import java.util.List;
import java.util.ArrayList;

public class Hospital  {

    private int phone;
    private String name;
    private String address;





    private List<Person> persons;




    private List<Person> persons;




    private Person person;


    public Hospital(
        int phone,        String name,        String address    ) {
        this.phone = phone;
        this.name = name;
        this.address = address;
        this.persons = new ArrayList<>();
        this.persons = new ArrayList<>();
    }

    public Hospital(
        int phone,        String name,        String address        ArrayList<Person> persons,        ArrayList<Person> persons    ) {
        this.phone = phone;
        this.name = name;
        this.address = address;
        this.persons = persons;
        this.persons = persons;
    }

    public int getPhone() {
        return phone;
    }

    public void setPhone(int phone) {
        this.phone = phone;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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