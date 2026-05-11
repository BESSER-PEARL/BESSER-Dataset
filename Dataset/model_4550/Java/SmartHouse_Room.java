





import java.util.List;
import java.util.ArrayList;

public class SmartHouse_Room  {

    private String bright;
    private String name;
    private int air;
    private float temp;





    private List<SmartHouse_Person> smarthouse_persons;




    private SmartHouse_House smarthouse_house;




    private SmartHouse_House smarthouse_house;


    public SmartHouse_Room(
        String bright,        String name,        int air,        float temp    ) {
        this.bright = bright;
        this.name = name;
        this.air = air;
        this.temp = temp;
        this.smarthouse_persons = new ArrayList<>();
    }

    public SmartHouse_Room(
        String bright,        String name,        int air,        float temp        ArrayList<SmartHouse_Person> smarthouse_persons    ) {
        this.bright = bright;
        this.name = name;
        this.air = air;
        this.temp = temp;
        this.smarthouse_persons = smarthouse_persons;
    }

    public String getBright() {
        return bright;
    }

    public void setBright(String bright) {
        this.bright = bright;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getAir() {
        return air;
    }

    public void setAir(int air) {
        this.air = air;
    }
    public float getTemp() {
        return temp;
    }

    public void setTemp(float temp) {
        this.temp = temp;
    }

    public List<SmartHouse_Person> getSmarthouse_persons() {
        return smarthouse_persons;
    }

    public void addSmarthouse_person(Smarthouse_person smarthouse_person) {
        this.smarthouse_persons.add(smarthouse_person);
    }
    public SmartHouse_House getSmarthouse_house() {
        return smarthouse_house;
    }

    public void setSmarthouse_house(SmartHouse_House smarthouse_house) {
        this.smarthouse_house = smarthouse_house;
    }
    public SmartHouse_House getSmarthouse_house() {
        return smarthouse_house;
    }

    public void setSmarthouse_house(SmartHouse_House smarthouse_house) {
        this.smarthouse_house = smarthouse_house;
    }

}