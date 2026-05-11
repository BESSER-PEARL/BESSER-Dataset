





import java.util.List;
import java.util.ArrayList;

public class restapp_model_PhysicalCard  {

    private int status;
    private int number;
    private int id;



    public restapp_model_PhysicalCard(
        int status,        int number,        int id    ) {
        this.status = status;
        this.number = number;
        this.id = id;
    }


    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}