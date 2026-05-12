





import java.util.List;
import java.util.ArrayList;

public class Person  {

    private int id;
    private String email;
    private String job;
    private String name;



    public Person(
        int id,        String email,        String job,        String name    ) {
        this.id = id;
        this.email = email;
        this.job = job;
        this.name = name;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
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


}