





import java.util.List;
import java.util.ArrayList;

public class SmartHouse_Person  {

    private String name;





    private SmartHouse_House smarthouse_house;


    public SmartHouse_Person(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SmartHouse_House getSmarthouse_house() {
        return smarthouse_house;
    }

    public void setSmarthouse_house(SmartHouse_House smarthouse_house) {
        this.smarthouse_house = smarthouse_house;
    }

}