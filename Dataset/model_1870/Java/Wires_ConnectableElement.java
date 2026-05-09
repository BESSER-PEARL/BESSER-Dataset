





import java.util.List;
import java.util.ArrayList;

public class Wires_ConnectableElement extends WiresElement {

    private String name;



    public Wires_ConnectableElement(
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