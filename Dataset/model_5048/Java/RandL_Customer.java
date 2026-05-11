





import java.util.List;
import java.util.ArrayList;

public class RandL_Customer  {

    private String isMale;
    private String name;
    private String age;
    private String gender;
    private String title;



    public RandL_Customer(
        String isMale,        String name,        String age,        String gender,        String title    ) {
        this.isMale = isMale;
        this.name = name;
        this.age = age;
        this.gender = gender;
        this.title = title;
    }


    public String getIsmale() {
        return isMale;
    }

    public void setIsmale(String isMale) {
        this.isMale = isMale;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}