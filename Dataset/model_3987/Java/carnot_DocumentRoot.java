





import java.util.List;
import java.util.ArrayList;

public class carnot_DocumentRoot  {

    private String mixed;





    private List<carnot_ModelType> carnot_modeltypes;


    public carnot_DocumentRoot(
        String mixed    ) {
        this.mixed = mixed;
        this.carnot_modeltypes = new ArrayList<>();
    }

    public carnot_DocumentRoot(
        String mixed        ArrayList<carnot_ModelType> carnot_modeltypes    ) {
        this.mixed = mixed;
        this.carnot_modeltypes = carnot_modeltypes;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<carnot_ModelType> getCarnot_modeltypes() {
        return carnot_modeltypes;
    }

    public void addCarnot_modeltype(Carnot_modeltype carnot_modeltype) {
        this.carnot_modeltypes.add(carnot_modeltype);
    }

}