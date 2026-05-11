





import java.util.List;
import java.util.ArrayList;

public class swrtj_Interface extends Element {






    private List<swrtj_Interface> swrtj_interfaces;


    public swrtj_Interface(
    ) {
        super(
        );
        this.swrtj_interfaces = new ArrayList<>();
    }

    public swrtj_Interface(
        ArrayList<swrtj_Interface> swrtj_interfaces    ) {
        this.swrtj_interfaces = swrtj_interfaces;
    }


    public List<swrtj_Interface> getSwrtj_interfaces() {
        return swrtj_interfaces;
    }

    public void addSwrtj_interface(Swrtj_interface swrtj_interface) {
        this.swrtj_interfaces.add(swrtj_interface);
    }

}