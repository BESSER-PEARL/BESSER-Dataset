





import java.util.List;
import java.util.ArrayList;

public class room_BaseState extends State {

    private String name;



    public room_BaseState(
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


}