





import java.util.List;
import java.util.ArrayList;

public class testing_Transition  {

    private String name;
    private String type;





    private testing_Adapter testing_adapter;


    public testing_Transition(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public testing_Adapter getTesting_adapter() {
        return testing_adapter;
    }

    public void setTesting_adapter(testing_Adapter testing_adapter) {
        this.testing_adapter = testing_adapter;
    }

}