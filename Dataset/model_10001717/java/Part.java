





import java.util.List;
import java.util.ArrayList;

public class Part  {

    private String _part_number;
    private String _description;





    private List<Part> parts;


    public Part(
        String _part_number,        String _description    ) {
        this._part_number = _part_number;
        this._description = _description;
        this.parts = new ArrayList<>();
    }

    public Part(
        String _part_number,        String _description        ArrayList<Part> parts    ) {
        this._part_number = _part_number;
        this._description = _description;
        this.parts = parts;
    }

    public String get_part_number() {
        return _part_number;
    }

    public void set_part_number(String _part_number) {
        this._part_number = _part_number;
    }
    public String get_description() {
        return _description;
    }

    public void set_description(String _description) {
        this._description = _description;
    }

    public List<Part> getParts() {
        return parts;
    }

    public void addPart(Part part) {
        this.parts.add(part);
    }

}