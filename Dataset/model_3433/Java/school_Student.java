





import java.util.List;
import java.util.ArrayList;

public class school_Student  {

    private String name;
    private int age;





    private school_Academy school_academy;


    public school_Student(
        String name,        int age    ) {
        this.name = name;
        this.age = age;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public school_Academy getSchool_academy() {
        return school_academy;
    }

    public void setSchool_academy(school_Academy school_academy) {
        this.school_academy = school_academy;
    }

}