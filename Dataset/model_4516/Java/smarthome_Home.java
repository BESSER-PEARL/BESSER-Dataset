





import java.util.List;
import java.util.ArrayList;

public class smarthome_Home  {

    private String fileEvents;





    private List<smarthome_NamedEntity> smarthome_namedentitys;




    private List<smarthome_Person> smarthome_persons;




    private List<smarthome_Room> smarthome_rooms;




    private List<smarthome_Pattern> smarthome_patterns;


    public smarthome_Home(
        String fileEvents    ) {
        this.fileEvents = fileEvents;
        this.smarthome_namedentitys = new ArrayList<>();
        this.smarthome_persons = new ArrayList<>();
        this.smarthome_rooms = new ArrayList<>();
        this.smarthome_patterns = new ArrayList<>();
    }

    public smarthome_Home(
        String fileEvents        ArrayList<smarthome_NamedEntity> smarthome_namedentitys,        ArrayList<smarthome_Person> smarthome_persons,        ArrayList<smarthome_Room> smarthome_rooms,        ArrayList<smarthome_Pattern> smarthome_patterns    ) {
        this.fileEvents = fileEvents;
        this.smarthome_namedentitys = smarthome_namedentitys;
        this.smarthome_persons = smarthome_persons;
        this.smarthome_rooms = smarthome_rooms;
        this.smarthome_patterns = smarthome_patterns;
    }

    public String getFileevents() {
        return fileEvents;
    }

    public void setFileevents(String fileEvents) {
        this.fileEvents = fileEvents;
    }

    public List<smarthome_NamedEntity> getSmarthome_namedentitys() {
        return smarthome_namedentitys;
    }

    public void addSmarthome_namedentity(Smarthome_namedentity smarthome_namedentity) {
        this.smarthome_namedentitys.add(smarthome_namedentity);
    }
    public List<smarthome_Person> getSmarthome_persons() {
        return smarthome_persons;
    }

    public void addSmarthome_person(Smarthome_person smarthome_person) {
        this.smarthome_persons.add(smarthome_person);
    }
    public List<smarthome_Room> getSmarthome_rooms() {
        return smarthome_rooms;
    }

    public void addSmarthome_room(Smarthome_room smarthome_room) {
        this.smarthome_rooms.add(smarthome_room);
    }
    public List<smarthome_Pattern> getSmarthome_patterns() {
        return smarthome_patterns;
    }

    public void addSmarthome_pattern(Smarthome_pattern smarthome_pattern) {
        this.smarthome_patterns.add(smarthome_pattern);
    }

}