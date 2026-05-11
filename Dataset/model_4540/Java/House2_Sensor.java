





import java.util.List;
import java.util.ArrayList;

public class House2_Sensor extends NamedElement {






    private House2_Container house2_container;




    private House2_Condition house2_condition;


    public House2_Sensor(
    ) {
        super(
        );
    }



    public House2_Container getHouse2_container() {
        return house2_container;
    }

    public void setHouse2_container(House2_Container house2_container) {
        this.house2_container = house2_container;
    }
    public House2_Condition getHouse2_condition() {
        return house2_condition;
    }

    public void setHouse2_condition(House2_Condition house2_condition) {
        this.house2_condition = house2_condition;
    }

}