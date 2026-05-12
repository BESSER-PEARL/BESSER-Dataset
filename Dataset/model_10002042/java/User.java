





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String gender;
    private String email;
    private String password;
    private String name;
    private String pages;
    private String groups;
    private String username;



    public User(
        String gender,        String email,        String password,        String name,        String pages,        String groups,        String username    ) {
        this.gender = gender;
        this.email = email;
        this.password = password;
        this.name = name;
        this.pages = pages;
        this.groups = groups;
        this.username = username;
    }


    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }


}