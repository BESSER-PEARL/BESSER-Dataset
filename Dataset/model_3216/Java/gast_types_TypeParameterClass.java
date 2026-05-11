





import java.util.List;
import java.util.ArrayList;

public class gast_types_TypeParameterClass extends GASTClass {






    private List<GASTType> gasttypes;


    public gast_types_TypeParameterClass(
    ) {
        super(
        );
        this.gasttypes = new ArrayList<>();
    }

    public gast_types_TypeParameterClass(
        ArrayList<GASTType> gasttypes    ) {
        this.gasttypes = gasttypes;
    }


    public List<GASTType> getGasttypes() {
        return gasttypes;
    }

    public void addGasttype(Gasttype gasttype) {
        this.gasttypes.add(gasttype);
    }

}