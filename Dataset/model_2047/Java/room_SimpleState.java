





import java.util.List;
import java.util.ArrayList;

public class room_SimpleState extends State {

    private String name;



    public room_SimpleState(
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