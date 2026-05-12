





import java.util.List;
import java.util.ArrayList;

public class Photos  {

    private String __photos;





    private User user;


    public Photos(
        String __photos    ) {
        this.__photos = __photos;
    }


    public String get__photos() {
        return __photos;
    }

    public void set__photos(String __photos) {
        this.__photos = __photos;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}