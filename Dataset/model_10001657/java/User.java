





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String password;
    private String gender;
    private String team;
    private String pages;
    private String username;
    private String phone;
    private String name;



    public User(
        String password,        String gender,        String team,        String pages,        String username,        String phone,        String name    ) {
        this.password = password;
        this.gender = gender;
        this.team = team;
        this.pages = pages;
        this.username = username;
        this.phone = phone;
        this.name = name;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public String getTeam() {
        return team;
    }

    public void setTeam(String team) {
        this.team = team;
    }
    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}