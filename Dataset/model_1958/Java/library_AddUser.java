





import java.util.List;
import java.util.ArrayList;

public class library_AddUser extends Command {

    private String secondname;
    private String age;
    private String firstname;



    public library_AddUser(
        String secondname,        String age,        String firstname    ) {
        super(
        );
        this.secondname = secondname;
        this.age = age;
        this.firstname = firstname;
    }


    public String getSecondname() {
        return secondname;
    }

    public void setSecondname(String secondname) {
        this.secondname = secondname;
    }
    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }


}