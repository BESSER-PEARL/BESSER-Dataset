





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String phone;
    private String pages;
    private String team;
    private String password;
    private String name;
    private String username;
    private String gender;



    public User(
        String phone,        String pages,        String team,        String password,        String name,        String username,        String gender    ) {
        this.phone = phone;
        this.pages = pages;
        this.team = team;
        this.password = password;
        this.name = name;
        this.username = username;
        this.gender = gender;
    }


    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
    }
    public String getTeam() {
        return team;
    }

    public void setTeam(String team) {
        this.team = team;
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
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }


}