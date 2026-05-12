





import java.util.List;
import java.util.ArrayList;

public class Hospital  {

    private String Address;
    private int HospitalId;
    private int Phone;
    private String Name;





    private List<Person> persons;


    public Hospital(
        String Address,        int HospitalId,        int Phone,        String Name    ) {
        this.Address = Address;
        this.HospitalId = HospitalId;
        this.Phone = Phone;
        this.Name = Name;
        this.persons = new ArrayList<>();
    }

    public Hospital(
        String Address,        int HospitalId,        int Phone,        String Name        ArrayList<Person> persons    ) {
        this.Address = Address;
        this.HospitalId = HospitalId;
        this.Phone = Phone;
        this.Name = Name;
        this.persons = persons;
    }

    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
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
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public List<Person> getPersons() {
        return persons;
    }

    public void addPerson(Person person) {
        this.persons.add(person);
    }

}