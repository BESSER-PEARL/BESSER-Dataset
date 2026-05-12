





import java.util.List;
import java.util.ArrayList;

public class Abstract_Component  {

    private String Type_Of_Component;



    public Abstract_Component(
        String Type_Of_Component    ) {
        this.Type_Of_Component = Type_Of_Component;
    }


    public String getType_of_component() {
        return Type_Of_Component;
    }

    public void setType_of_component(String Type_Of_Component) {
        this.Type_Of_Component = Type_Of_Component;
    }


}