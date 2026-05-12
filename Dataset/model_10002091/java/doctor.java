





import java.util.List;
import java.util.ArrayList;

public class doctor  {

    private String grade;
    private String name;
    private String address;



    public doctor(
        String grade,        String name,        String address    ) {
        this.grade = grade;
        this.name = name;
        this.address = address;
    }


    public String getGrade() {
        return grade;
    }

    public void setGrade(String grade) {
        this.grade = grade;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}