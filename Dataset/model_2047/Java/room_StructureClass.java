





import java.util.List;
import java.util.ArrayList;

public class room_StructureClass extends RoomClass {






    private List<room_LayerConnection> room_layerconnections;




    private List<room_Binding> room_bindings;


    public room_StructureClass(
    ) {
        super(
        );
        this.room_layerconnections = new ArrayList<>();
        this.room_bindings = new ArrayList<>();
    }

    public room_StructureClass(
        ArrayList<room_LayerConnection> room_layerconnections,        ArrayList<room_Binding> room_bindings    ) {
        this.room_layerconnections = room_layerconnections;
        this.room_bindings = room_bindings;
    }


    public List<room_LayerConnection> getRoom_layerconnections() {
        return room_layerconnections;
    }

    public void addRoom_layerconnection(Room_layerconnection room_layerconnection) {
        this.room_layerconnections.add(room_layerconnection);
    }
    public List<room_Binding> getRoom_bindings() {
        return room_bindings;
    }

    public void addRoom_binding(Room_binding room_binding) {
        this.room_bindings.add(room_binding);
    }

}