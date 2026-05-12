





import java.util.List;
import java.util.ArrayList;

public class Instructor  {

    private String name;





    private Checking checking;


    public Instructor(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Checking getChecking() {
        return checking;
    }

    public void setChecking(Checking checking) {
        this.checking = checking;
    }

}