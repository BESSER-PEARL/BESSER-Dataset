





import java.util.List;
import java.util.ArrayList;

public class model_Resident  {

    private String firstName;
    private String surname;
    private String id;





    private model_Room model_room;


    public model_Resident(
        String firstName,        String surname,        String id    ) {
        this.firstName = firstName;
        this.surname = surname;
        this.id = id;
    }


    public String getFirstname() {
        return firstName;
    }

    public void setFirstname(String firstName) {
        this.firstName = firstName;
    }
    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public model_Room getModel_room() {
        return model_room;
    }

    public void setModel_room(model_Room model_room) {
        this.model_room = model_room;
    }

}