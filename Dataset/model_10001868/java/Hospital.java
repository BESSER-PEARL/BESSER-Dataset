





import java.util.List;
import java.util.ArrayList;

public class Hospital  {

    private String phone;
    private String address;
    private String name;





    private List<Person> persons;


    public Hospital(
        String phone,        String address,        String name    ) {
        this.phone = phone;
        this.address = address;
        this.name = name;
        this.persons = new ArrayList<>();
    }

    public Hospital(
        String phone,        String address,        String name        ArrayList<Person> persons    ) {
        this.phone = phone;
        this.address = address;
        this.name = name;
        this.persons = persons;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
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

    public List<Person> getPersons() {
        return persons;
    }

    public void addPerson(Person person) {
        this.persons.add(person);
    }

}