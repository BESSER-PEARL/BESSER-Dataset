





import java.util.List;
import java.util.ArrayList;

public class Person  {

    private String username;
    private String date_of_birth;
    private String email;
    private int id;
    private String name;
    private String department;
    private String address;
    private int password;



    public Person(
        String username,        String date_of_birth,        String email,        int id,        String name,        String department,        String address,        int password    ) {
        this.username = username;
        this.date_of_birth = date_of_birth;
        this.email = email;
        this.id = id;
        this.name = name;
        this.department = department;
        this.address = address;
        this.password = password;
    }


    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getDate_of_birth() {
        return date_of_birth;
    }

    public void setDate_of_birth(String date_of_birth) {
        this.date_of_birth = date_of_birth;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getPassword() {
        return password;
    }

    public void setPassword(int password) {
        this.password = password;
    }


}