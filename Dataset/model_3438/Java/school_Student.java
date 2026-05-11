





import java.util.List;
import java.util.ArrayList;

public class school_Student  {

    private int age;
    private String nickname;
    private String name;





    private school_Student school_student;




    private school_Classroom school_classroom;


    public school_Student(
        int age,        String nickname,        String name    ) {
        this.age = age;
        this.nickname = nickname;
        this.name = name;
    }


    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
    public String getNickname() {
        return nickname;
    }

    public void setNickname(String nickname) {
        this.nickname = nickname;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public school_Student getSchool_student() {
        return school_student;
    }

    public void setSchool_student(school_Student school_student) {
        this.school_student = school_student;
    }
    public school_Classroom getSchool_classroom() {
        return school_classroom;
    }

    public void setSchool_classroom(school_Classroom school_classroom) {
        this.school_classroom = school_classroom;
    }

}