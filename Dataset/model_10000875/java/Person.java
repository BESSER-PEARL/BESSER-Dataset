





import java.util.List;
import java.util.ArrayList;

public class Person  {

    private String department;
    private String username;
    private String address;
    private String date_of_birth;
    private int id;
    private int password;
    private String name;
    private String email;



    public Person(
        String department,        String username,        String address,        String date_of_birth,        int id,        int password,        String name,        String email    ) {
        this.department = department;
        this.username = username;
        this.address = address;
        this.date_of_birth = date_of_birth;
        this.id = id;
        this.password = password;
        this.name = name;
        this.email = email;
    }


    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getDate_of_birth() {
        return date_of_birth;
    }

    public void setDate_of_birth(String date_of_birth) {
        this.date_of_birth = date_of_birth;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
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
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}