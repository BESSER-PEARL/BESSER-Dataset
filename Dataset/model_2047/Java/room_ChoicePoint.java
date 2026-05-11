





import java.util.List;
import java.util.ArrayList;

public class room_ChoicePoint extends StateGraphNode {

    private String name;





    private room_StateGraph room_stategraph;




    private room_Documentation room_documentation;


    public room_ChoicePoint(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public room_StateGraph getRoom_stategraph() {
        return room_stategraph;
    }

    public void setRoom_stategraph(room_StateGraph room_stategraph) {
        this.room_stategraph = room_stategraph;
    }
    public room_Documentation getRoom_documentation() {
        return room_documentation;
    }

    public void setRoom_documentation(room_Documentation room_documentation) {
        this.room_documentation = room_documentation;
    }

}