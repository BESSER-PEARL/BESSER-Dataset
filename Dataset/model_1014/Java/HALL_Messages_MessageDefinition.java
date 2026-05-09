





import java.util.List;
import java.util.ArrayList;

public class HALL_Messages_MessageDefinition  {

    private String name;





    private List<Messages_HALL_Data> messages_hall_datas;


    public HALL_Messages_MessageDefinition(
        String name    ) {
        this.name = name;
        this.messages_hall_datas = new ArrayList<>();
    }

    public HALL_Messages_MessageDefinition(
        String name        ArrayList<Messages_HALL_Data> messages_hall_datas    ) {
        this.name = name;
        this.messages_hall_datas = messages_hall_datas;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Messages_HALL_Data> getMessages_hall_datas() {
        return messages_hall_datas;
    }

    public void addMessages_hall_data(Messages_hall_data messages_hall_data) {
        this.messages_hall_datas.add(messages_hall_data);
    }

}