




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_User  {

    private LocalDate birthDate;
    private String sex;
    private String name;
    private String userId;





    private model_User model_user;




    private List<model_User> model_users;


    public model_User(
        LocalDate birthDate,        String sex,        String name,        String userId    ) {
        this.birthDate = birthDate;
        this.sex = sex;
        this.name = name;
        this.userId = userId;
        this.model_users = new ArrayList<>();
    }

    public model_User(
        LocalDate birthDate,        String sex,        String name,        String userId        ArrayList<model_User> model_users    ) {
        this.birthDate = birthDate;
        this.sex = sex;
        this.name = name;
        this.userId = userId;
        this.model_users = model_users;
    }

    public LocalDate getBirthdate() {
        return birthDate;
    }

    public void setBirthdate(LocalDate birthDate) {
        this.birthDate = birthDate;
    }
    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
    }

    public model_User getModel_user() {
        return model_user;
    }

    public void setModel_user(model_User model_user) {
        this.model_user = model_user;
    }
    public List<model_User> getModel_users() {
        return model_users;
    }

    public void addModel_user(Model_user model_user) {
        this.model_users.add(model_user);
    }

}