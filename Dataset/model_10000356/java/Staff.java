





import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private String job;
    private String name;





    private Person person;


    public Staff(
        String job,        String name    ) {
        this.job = job;
        this.name = name;
    }


    public String getJob() {
        return job;
    }

    public void setJob(String job) {
        this.job = job;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Person getPerson() {
        return person;
    }

    public void setPerson(Person person) {
        this.person = person;
    }

}