





import java.util.List;
import java.util.ArrayList;

public class gast_accesses_TypeAccess extends Access {






    private GASTType gasttype;




    private List<GASTType> gasttypes;


    public gast_accesses_TypeAccess(
    ) {
        super(
        );
        this.gasttypes = new ArrayList<>();
    }

    public gast_accesses_TypeAccess(
        ArrayList<GASTType> gasttypes    ) {
        this.gasttypes = gasttypes;
    }


    public GASTType getGasttype() {
        return gasttype;
    }

    public void setGasttype(GASTType gasttype) {
        this.gasttype = gasttype;
    }
    public List<GASTType> getGasttypes() {
        return gasttypes;
    }

    public void addGasttype(Gasttype gasttype) {
        this.gasttypes.add(gasttype);
    }

}