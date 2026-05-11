





import java.util.List;
import java.util.ArrayList;

public class room_ChoicePoint extends StateGraphNode {

    private String name;





    private room_StateGraph room_stategraph;


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

}