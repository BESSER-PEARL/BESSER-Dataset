





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String email;
    private String gender;
    private String name;
    private String username;
    private String pages;
    private String groups;
    private String password;



    public User(
        String email,        String gender,        String name,        String username,        String pages,        String groups,        String password    ) {
        this.email = email;
        this.gender = gender;
        this.name = name;
        this.username = username;
        this.pages = pages;
        this.groups = groups;
        this.password = password;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
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
    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
    }
    public String getGroups() {
        return groups;
    }

    public void setGroups(String groups) {
        this.groups = groups;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }


}