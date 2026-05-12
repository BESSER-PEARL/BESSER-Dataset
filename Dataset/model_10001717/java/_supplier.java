





import java.util.List;
import java.util.ArrayList;

public class _supplier  {

    private String _supplier_ID;





    private List<Part> parts;


    public _supplier(
        String _supplier_ID    ) {
        this._supplier_ID = _supplier_ID;
        this.parts = new ArrayList<>();
    }

    public _supplier(
        String _supplier_ID        ArrayList<Part> parts    ) {
        this._supplier_ID = _supplier_ID;
        this.parts = parts;
    }

    public String get_supplier_id() {
        return _supplier_ID;
    }

    public void set_supplier_id(String _supplier_ID) {
        this._supplier_ID = _supplier_ID;
    }

    public List<Part> getParts() {
        return parts;
    }

    public void addPart(Part part) {
        this.parts.add(part);
    }

}