





import java.util.List;
import java.util.ArrayList;

public class Person  {

    private String name;
    private String Birth_date;
    private String father_s_name;
    private int Age;
    private String Gender;





    private Hospital hospital;


    public Person(
        String name,        String Birth_date,        String father_s_name,        int Age,        String Gender    ) {
        this.name = name;
        this.Birth_date = Birth_date;
        this.father_s_name = father_s_name;
        this.Age = Age;
        this.Gender = Gender;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getBirth_date() {
        return Birth_date;
    }

    public void setBirth_date(String Birth_date) {
        this.Birth_date = Birth_date;
    }
    public String getFather_s_name() {
        return father_s_name;
    }

    public void setFather_s_name(String father_s_name) {
        this.father_s_name = father_s_name;
    }
    public int getAge() {
        return Age;
    }

    public void setAge(int Age) {
        this.Age = Age;
    }
    public String getGender() {
        return Gender;
    }

    public void setGender(String Gender) {
        this.Gender = Gender;
    }

    public Hospital getHospital() {
        return hospital;
    }

    public void setHospital(Hospital hospital) {
        this.hospital = hospital;
    }

}