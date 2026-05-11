





import java.util.List;
import java.util.ArrayList;

public class diva_Dimension extends NamedElement {

    private String lower;
    private String upper;





    private List<diva_Property> diva_propertys;


    public diva_Dimension(
        String lower,        String upper    ) {
        super(
        );
        this.lower = lower;
        this.upper = upper;
        this.diva_propertys = new ArrayList<>();
    }

    public diva_Dimension(
        String lower,        String upper        ArrayList<diva_Property> diva_propertys    ) {
        this.lower = lower;
        this.upper = upper;
        this.diva_propertys = diva_propertys;
    }

    public String getLower() {
        return lower;
    }

    public void setLower(String lower) {
        this.lower = lower;
    }
    public String getUpper() {
        return upper;
    }

    public void setUpper(String upper) {
        this.upper = upper;
    }

    public List<diva_Property> getDiva_propertys() {
        return diva_propertys;
    }

    public void addDiva_property(Diva_property diva_property) {
        this.diva_propertys.add(diva_property);
    }

}