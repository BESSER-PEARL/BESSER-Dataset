





import java.util.List;
import java.util.ArrayList;

public class HALL_Data  {

    private String currentValue;
    private String name;
    private String initValue;
    private String type;





    private HALL_Component hall_component;




    private HALL_Component hall_component;


    public HALL_Data(
        String currentValue,        String name,        String initValue,        String type    ) {
        this.currentValue = currentValue;
        this.name = name;
        this.initValue = initValue;
        this.type = type;
    }


    public String getCurrentvalue() {
        return currentValue;
    }

    public void setCurrentvalue(String currentValue) {
        this.currentValue = currentValue;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getInitvalue() {
        return initValue;
    }

    public void setInitvalue(String initValue) {
        this.initValue = initValue;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public HALL_Component getHall_component() {
        return hall_component;
    }

    public void setHall_component(HALL_Component hall_component) {
        this.hall_component = hall_component;
    }
    public HALL_Component getHall_component() {
        return hall_component;
    }

    public void setHall_component(HALL_Component hall_component) {
        this.hall_component = hall_component;
    }

}