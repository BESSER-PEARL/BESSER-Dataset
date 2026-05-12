





import java.util.List;
import java.util.ArrayList;

public class Hospital  {

    private String Address;
    private String Name;
    private int HospitalId;
    private int Phone;





    private List<Person> persons;


    public Hospital(
        String Address,        String Name,        int HospitalId,        int Phone    ) {
        this.Address = Address;
        this.Name = Name;
        this.HospitalId = HospitalId;
        this.Phone = Phone;
        this.persons = new ArrayList<>();
    }

    public Hospital(
        String Address,        String Name,        int HospitalId,        int Phone        ArrayList<Person> persons    ) {
        this.Address = Address;
        this.Name = Name;
        this.HospitalId = HospitalId;
        this.Phone = Phone;
        this.persons = persons;
    }

    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getHospitalid() {
        return HospitalId;
    }

    public void setHospitalid(int HospitalId) {
        this.HospitalId = HospitalId;
    }
    public int getPhone() {
        return Phone;
    }

    public void setPhone(int Phone) {
        this.Phone = Phone;
    }

    public List<Person> getPersons() {
        return persons;
    }

    public void addPerson(Person person) {
        this.persons.add(person);
    }

}