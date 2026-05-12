





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String name;
    private String username;
    private String email;
    private String password;
    private String groups;
    private String gender;
    private String pages;



    public User(
        String name,        String username,        String email,        String password,        String groups,        String gender,        String pages    ) {
        this.name = name;
        this.username = username;
        this.email = email;
        this.password = password;
        this.groups = groups;
        this.gender = gender;
        this.pages = pages;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getGroups() {
        return groups;
    }

    public void setGroups(String groups) {
        this.groups = groups;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
    }


}