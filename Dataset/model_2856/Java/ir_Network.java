





import java.util.List;
import java.util.ArrayList;

public class ir_Network extends AbstractActor {






    private List<ir_Connection> ir_connections;


    public ir_Network(
    ) {
        super(
        );
        this.ir_connections = new ArrayList<>();
    }

    public ir_Network(
        ArrayList<ir_Connection> ir_connections    ) {
        this.ir_connections = ir_connections;
    }


    public List<ir_Connection> getIr_connections() {
        return ir_connections;
    }

    public void addIr_connection(Ir_connection ir_connection) {
        this.ir_connections.add(ir_connection);
    }

}