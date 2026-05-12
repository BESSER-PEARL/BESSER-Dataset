




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Models_LoginLog  {

    private LocalDate lastLoginDate;
    private int id;
    private int user_id;
    private boolean isLogin;





    private Models_User models_user;


    public Models_LoginLog(
        LocalDate lastLoginDate,        int id,        int user_id,        boolean isLogin    ) {
        this.lastLoginDate = lastLoginDate;
        this.id = id;
        this.user_id = user_id;
        this.isLogin = isLogin;
    }


    public LocalDate getLastlogindate() {
        return lastLoginDate;
    }

    public void setLastlogindate(LocalDate lastLoginDate) {
        this.lastLoginDate = lastLoginDate;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getUser_id() {
        return user_id;
    }

    public void setUser_id(int user_id) {
        this.user_id = user_id;
    }
    public boolean getIslogin() {
        return isLogin;
    }

    public void setIslogin(boolean isLogin) {
        this.isLogin = isLogin;
    }

    public Models_User getModels_user() {
        return models_user;
    }

    public void setModels_user(Models_User models_user) {
        this.models_user = models_user;
    }

}