





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String healthrecords;
    private String name;
    private int id;





    private Person person;


    public Patient(
        String healthrecords,        String name,        int id    ) {
        this.healthrecords = healthrecords;
        this.name = name;
        this.id = id;
    }


    public String getHealthrecords() {
        return healthrecords;
    }

    public void setHealthrecords(String healthrecords) {
        this.healthrecords = healthrecords;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Person getPerson() {
        return person;
    }

    public void setPerson(Person person) {
        this.person = person;
    }

}