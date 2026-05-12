





import java.util.List;
import java.util.ArrayList;

public class Person  {

    private String username;
    private int id;
    private String date_of_birth;
    private String department;
    private int password;
    private String name;
    private String address;
    private String email;



    public Person(
        String username,        int id,        String date_of_birth,        String department,        int password,        String name,        String address,        String email    ) {
        this.username = username;
        this.id = id;
        this.date_of_birth = date_of_birth;
        this.department = department;
        this.password = password;
        this.name = name;
        this.address = address;
        this.email = email;
    }


    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getDate_of_birth() {
        return date_of_birth;
    }

    public void setDate_of_birth(String date_of_birth) {
        this.date_of_birth = date_of_birth;
    }
    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }
    public int getPassword() {
        return password;
    }

    public void setPassword(int password) {
        this.password = password;
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
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}