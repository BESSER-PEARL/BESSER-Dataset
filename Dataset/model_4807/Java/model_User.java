




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_User  {

    private String userId;
    private String sex;
    private LocalDate birthDate;
    private String name;





    private model_User model_user;




    private model_User model_user;


    public model_User(
        String userId,        String sex,        LocalDate birthDate,        String name    ) {
        this.userId = userId;
        this.sex = sex;
        this.birthDate = birthDate;
        this.name = name;
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
    public LocalDate getBirthdate() {
        return birthDate;
    }

    public void setBirthdate(LocalDate birthDate) {
        this.birthDate = birthDate;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_User getModel_user() {
        return model_user;
    }

    public void setModel_user(model_User model_user) {
        this.model_user = model_user;
    }
    public model_User getModel_user() {
        return model_user;
    }

    public void setModel_user(model_User model_user) {
        this.model_user = model_user;
    }

}