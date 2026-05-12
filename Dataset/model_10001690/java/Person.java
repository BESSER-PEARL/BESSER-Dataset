





import java.util.List;
import java.util.ArrayList;

public class Person  {

    private String Name1;
    private String Phone_no;
    private int Age;
    private String Birth_date;
    private String Name;
    private String Gender;
    private String Id;



    public Person(
        String Name1,        String Phone_no,        int Age,        String Birth_date,        String Name,        String Gender,        String Id    ) {
        this.Name1 = Name1;
        this.Phone_no = Phone_no;
        this.Age = Age;
        this.Birth_date = Birth_date;
        this.Name = Name;
        this.Gender = Gender;
        this.Id = Id;
    }


    public String getName1() {
        return Name1;
    }

    public void setName1(String Name1) {
        this.Name1 = Name1;
    }
    public String getPhone_no() {
        return Phone_no;
    }

    public void setPhone_no(String Phone_no) {
        this.Phone_no = Phone_no;
    }
    public int getAge() {
        return Age;
    }

    public void setAge(int Age) {
        this.Age = Age;
    }
    public String getBirth_date() {
        return Birth_date;
    }

    public void setBirth_date(String Birth_date) {
        this.Birth_date = Birth_date;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getGender() {
        return Gender;
    }

    public void setGender(String Gender) {
        this.Gender = Gender;
    }
    public String getId() {
        return Id;
    }

    public void setId(String Id) {
        this.Id = Id;
    }


}