





import java.util.List;
import java.util.ArrayList;

public class User  {

    private int age;
    private String email;
    private String username;
    private int phone;
    private String name;
    private String gender;
    private String password;



    public User(
        int age,        String email,        String username,        int phone,        String name,        String gender,        String password    ) {
        this.age = age;
        this.email = email;
        this.username = username;
        this.phone = phone;
        this.name = name;
        this.gender = gender;
        this.password = password;
    }


    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public int getPhone() {
        return phone;
    }

    public void setPhone(int phone) {
        this.phone = phone;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}