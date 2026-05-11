




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_User  {

    private String userId;
    private String sex;
    private String name;
    private LocalDate birthDate;





    private List<model_User> model_users;




    private model_User model_user;


    public model_User(
        String userId,        String sex,        String name,        LocalDate birthDate    ) {
        this.userId = userId;
        this.sex = sex;
        this.name = name;
        this.birthDate = birthDate;
        this.model_users = new ArrayList<>();
    }

    public model_User(
        String userId,        String sex,        String name,        LocalDate birthDate        ArrayList<model_User> model_users    ) {
        this.userId = userId;
        this.sex = sex;
        this.name = name;
        this.birthDate = birthDate;
        this.model_users = model_users;
    }

    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
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
    public LocalDate getBirthdate() {
        return birthDate;
    }

    public void setBirthdate(LocalDate birthDate) {
        this.birthDate = birthDate;
    }

    public List<model_User> getModel_users() {
        return model_users;
    }

    public void addModel_user(Model_user model_user) {
        this.model_users.add(model_user);
    }
    public model_User getModel_user() {
        return model_user;
    }

    public void setModel_user(model_User model_user) {
        this.model_user = model_user;
    }

}