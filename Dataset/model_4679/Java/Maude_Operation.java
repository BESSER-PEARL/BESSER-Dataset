





import java.util.List;
import java.util.ArrayList;

public class Maude_Operation extends ModElement {

    private String atts;
    private String name;





    private List<Maude_Type> maude_types;




    private Maude_Type maude_type;


    public Maude_Operation(
        String atts,        String name    ) {
        super(
        );
        this.atts = atts;
        this.name = name;
        this.maude_types = new ArrayList<>();
    }

    public Maude_Operation(
        String atts,        String name        ArrayList<Maude_Type> maude_types    ) {
        this.atts = atts;
        this.name = name;
        this.maude_types = maude_types;
    }

    public String getAtts() {
        return atts;
    }

    public void setAtts(String atts) {
        this.atts = atts;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Maude_Type> getMaude_types() {
        return maude_types;
    }

    public void addMaude_type(Maude_type maude_type) {
        this.maude_types.add(maude_type);
    }
    public Maude_Type getMaude_type() {
        return maude_type;
    }

    public void setMaude_type(Maude_Type maude_type) {
        this.maude_type = maude_type;
    }

}