





import java.util.List;
import java.util.ArrayList;

public class student_record  {

    private String name;
    private String fines;
    private String phone_number;
    private String address;





    private student student;


    public student_record(
        String name,        String fines,        String phone_number,        String address    ) {
        this.name = name;
        this.fines = fines;
        this.phone_number = phone_number;
        this.address = address;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFines() {
        return fines;
    }

    public void setFines(String fines) {
        this.fines = fines;
    }
    public String getPhone_number() {
        return phone_number;
    }

    public void setPhone_number(String phone_number) {
        this.phone_number = phone_number;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public student getStudent() {
        return student;
    }

    public void setStudent(student student) {
        this.student = student;
    }

}