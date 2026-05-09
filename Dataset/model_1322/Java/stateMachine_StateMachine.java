





import java.util.List;
import java.util.ArrayList;

public class stateMachine_StateMachine  {

    private String name;
    private String package;



    public stateMachine_StateMachine(
        String name,        String package    ) {
        this.name = name;
        this.package = package;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPackage() {
        return package;
    }

    public void setPackage(String package) {
        this.package = package;
    }


}