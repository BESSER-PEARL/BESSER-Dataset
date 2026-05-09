





import java.util.List;
import java.util.ArrayList;

public class simpleparts_Thing extends NamedElement {

    private int id;





    private List<simpleparts_Part> simpleparts_parts;




    private List<simpleparts_Item> simpleparts_items;




    private simpleparts_World simpleparts_world;




    private List<simpleparts_Element> simpleparts_elements;




    private List<simpleparts_Piece> simpleparts_pieces;


    public simpleparts_Thing(
        int id    ) {
        super(
        );
        this.id = id;
        this.simpleparts_parts = new ArrayList<>();
        this.simpleparts_items = new ArrayList<>();
        this.simpleparts_elements = new ArrayList<>();
        this.simpleparts_pieces = new ArrayList<>();
    }

    public simpleparts_Thing(
        int id        ArrayList<simpleparts_Part> simpleparts_parts,        ArrayList<simpleparts_Item> simpleparts_items,        ArrayList<simpleparts_Element> simpleparts_elements,        ArrayList<simpleparts_Piece> simpleparts_pieces    ) {
        this.id = id;
        this.simpleparts_parts = simpleparts_parts;
        this.simpleparts_items = simpleparts_items;
        this.simpleparts_elements = simpleparts_elements;
        this.simpleparts_pieces = simpleparts_pieces;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<simpleparts_Part> getSimpleparts_parts() {
        return simpleparts_parts;
    }

    public void addSimpleparts_part(Simpleparts_part simpleparts_part) {
        this.simpleparts_parts.add(simpleparts_part);
    }
    public List<simpleparts_Item> getSimpleparts_items() {
        return simpleparts_items;
    }

    public void addSimpleparts_item(Simpleparts_item simpleparts_item) {
        this.simpleparts_items.add(simpleparts_item);
    }
    public simpleparts_World getSimpleparts_world() {
        return simpleparts_world;
    }

    public void setSimpleparts_world(simpleparts_World simpleparts_world) {
        this.simpleparts_world = simpleparts_world;
    }
    public List<simpleparts_Element> getSimpleparts_elements() {
        return simpleparts_elements;
    }

    public void addSimpleparts_element(Simpleparts_element simpleparts_element) {
        this.simpleparts_elements.add(simpleparts_element);
    }
    public List<simpleparts_Piece> getSimpleparts_pieces() {
        return simpleparts_pieces;
    }

    public void addSimpleparts_piece(Simpleparts_piece simpleparts_piece) {
        this.simpleparts_pieces.add(simpleparts_piece);
    }

}