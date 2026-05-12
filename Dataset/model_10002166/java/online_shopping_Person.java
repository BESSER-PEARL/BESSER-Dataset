





import java.util.List;
import java.util.ArrayList;

public class online_shopping_Person  {

    private None Person_ID;
    private None Login_Status;
    private None Person_Password;



    public online_shopping_Person(
        None Person_ID,        None Login_Status,        None Person_Password    ) {
        this.Person_ID = Person_ID;
        this.Login_Status = Login_Status;
        this.Person_Password = Person_Password;
    }


    public None getPerson_id() {
        return Person_ID;
    }

    public void setPerson_id(None Person_ID) {
        this.Person_ID = Person_ID;
    }
    public None getLogin_status() {
        return Login_Status;
    }

    public void setLogin_status(None Login_Status) {
        this.Login_Status = Login_Status;
    }
    public None getPerson_password() {
        return Person_Password;
    }

    public void setPerson_password(None Person_Password) {
        this.Person_Password = Person_Password;
    }


}