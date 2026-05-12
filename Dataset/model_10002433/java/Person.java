





import java.util.List;
import java.util.ArrayList;

public class Person  {

    private String name_;
    private String password_;
    private String id_;
    private String phone_;



    public Person(
        String name_,        String password_,        String id_,        String phone_    ) {
        this.name_ = name_;
        this.password_ = password_;
        this.id_ = id_;
        this.phone_ = phone_;
    }


    public String getName_() {
        return name_;
    }

    public void setName_(String name_) {
        this.name_ = name_;
    }
    public String getPassword_() {
        return password_;
    }

    public void setPassword_(String password_) {
        this.password_ = password_;
    }
    public String getId_() {
        return id_;
    }

    public void setId_(String id_) {
        this.id_ = id_;
    }
    public String getPhone_() {
        return phone_;
    }

    public void setPhone_(String phone_) {
        this.phone_ = phone_;
    }


}