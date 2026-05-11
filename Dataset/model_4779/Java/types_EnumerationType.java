





import java.util.List;
import java.util.ArrayList;

public class types_EnumerationType extends ComplexType {






    private types_Enumerator types_enumerator;




    private List<types_Enumerator> types_enumerators;


    public types_EnumerationType(
    ) {
        super(
        );
        this.types_enumerators = new ArrayList<>();
    }

    public types_EnumerationType(
        ArrayList<types_Enumerator> types_enumerators    ) {
        this.types_enumerators = types_enumerators;
    }


    public types_Enumerator getTypes_enumerator() {
        return types_enumerator;
    }

    public void setTypes_enumerator(types_Enumerator types_enumerator) {
        this.types_enumerator = types_enumerator;
    }
    public List<types_Enumerator> getTypes_enumerators() {
        return types_enumerators;
    }

    public void addTypes_enumerator(Types_enumerator types_enumerator) {
        this.types_enumerators.add(types_enumerator);
    }

}