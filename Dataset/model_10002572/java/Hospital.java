





import java.util.List;
import java.util.ArrayList;

public class Hospital  {

    private String address;
    private String name;
    private String phone;





    private List<Person> persons;


    public Hospital(
        String address,        String name,        String phone    ) {
        this.address = address;
        this.name = name;
        this.phone = phone;
        this.persons = new ArrayList<>();
    }

    public Hospital(
        String address,        String name,        String phone        ArrayList<Person> persons    ) {
        this.address = address;
        this.name = name;
        this.phone = phone;
        this.persons = persons;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public List<Person> getPersons() {
        return persons;
    }

    public void addPerson(Person person) {
        this.persons.add(person);
    }

}