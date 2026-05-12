





import java.util.List;
import java.util.ArrayList;

public class Project  {

    private None status;
    private String name;



    public Project(
        None status,        String name    ) {
        this.status = status;
        this.name = name;
    }


    public None getStatus() {
        return status;
    }

    public void setStatus(None status) {
        this.status = status;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}