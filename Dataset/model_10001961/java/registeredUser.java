





import java.util.List;
import java.util.ArrayList;

public class registeredUser  {

    private String Status;
    private int Id;



    public registeredUser(
        String Status,        int Id    ) {
        this.Status = Status;
        this.Id = Id;
    }


    public String getStatus() {
        return Status;
    }

    public void setStatus(String Status) {
        this.Status = Status;
    }
    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }


}