





import java.util.List;
import java.util.ArrayList;

public class transport_PacketStyleTransportSystem extends TransportSystem {






    private List<transport_LoadUnloadEdge> transport_loadunloadedges;




    private List<transport_LoadUnloadEdge> transport_loadunloadedges;


    public transport_PacketStyleTransportSystem(
    ) {
        super(
        );
        this.transport_loadunloadedges = new ArrayList<>();
        this.transport_loadunloadedges = new ArrayList<>();
    }

    public transport_PacketStyleTransportSystem(
        ArrayList<transport_LoadUnloadEdge> transport_loadunloadedges,        ArrayList<transport_LoadUnloadEdge> transport_loadunloadedges    ) {
        this.transport_loadunloadedges = transport_loadunloadedges;
        this.transport_loadunloadedges = transport_loadunloadedges;
    }


    public List<transport_LoadUnloadEdge> getTransport_loadunloadedges() {
        return transport_loadunloadedges;
    }

    public void addTransport_loadunloadedge(Transport_loadunloadedge transport_loadunloadedge) {
        this.transport_loadunloadedges.add(transport_loadunloadedge);
    }
    public List<transport_LoadUnloadEdge> getTransport_loadunloadedges() {
        return transport_loadunloadedges;
    }

    public void addTransport_loadunloadedge(Transport_loadunloadedge transport_loadunloadedge) {
        this.transport_loadunloadedges.add(transport_loadunloadedge);
    }

}