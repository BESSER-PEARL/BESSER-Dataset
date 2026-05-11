





import java.util.List;
import java.util.ArrayList;

public class diva_Property extends NamedElement {

    private String direction;





    private List<diva_PropertyLiteral> diva_propertyliterals;




    private diva_Dimension diva_dimension;


    public diva_Property(
        String direction    ) {
        super(
        );
        this.direction = direction;
        this.diva_propertyliterals = new ArrayList<>();
    }

    public diva_Property(
        String direction        ArrayList<diva_PropertyLiteral> diva_propertyliterals    ) {
        this.direction = direction;
        this.diva_propertyliterals = diva_propertyliterals;
    }

    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }

    public List<diva_PropertyLiteral> getDiva_propertyliterals() {
        return diva_propertyliterals;
    }

    public void addDiva_propertyliteral(Diva_propertyliteral diva_propertyliteral) {
        this.diva_propertyliterals.add(diva_propertyliteral);
    }
    public diva_Dimension getDiva_dimension() {
        return diva_dimension;
    }

    public void setDiva_dimension(diva_Dimension diva_dimension) {
        this.diva_dimension = diva_dimension;
    }

}