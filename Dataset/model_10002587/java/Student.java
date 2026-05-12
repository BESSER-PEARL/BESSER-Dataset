





import java.util.List;
import java.util.ArrayList;

public class Student  {

    private String name;
    private int Phone;
    private int Age;





    private Teacher teacher;


    public Student(
        String name,        int Phone,        int Age    ) {
        this.name = name;
        this.Phone = Phone;
        this.Age = Age;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getPhone() {
        return Phone;
    }

    public void setPhone(int Phone) {
        this.Phone = Phone;
    }
    public int getAge() {
        return Age;
    }

    public void setAge(int Age) {
        this.Age = Age;
    }

    public Teacher getTeacher() {
        return teacher;
    }

    public void setTeacher(Teacher teacher) {
        this.teacher = teacher;
    }

}