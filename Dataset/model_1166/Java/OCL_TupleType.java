





import java.util.List;
import java.util.ArrayList;

public class OCL_TupleType extends OclType {






    private List<TupleTypeAttribute> tupletypeattributes;


    public OCL_TupleType(
    ) {
        super(
        );
        this.tupletypeattributes = new ArrayList<>();
    }

    public OCL_TupleType(
        ArrayList<TupleTypeAttribute> tupletypeattributes    ) {
        this.tupletypeattributes = tupletypeattributes;
    }


    public List<TupleTypeAttribute> getTupletypeattributes() {
        return tupletypeattributes;
    }

    public void addTupletypeattribute(Tupletypeattribute tupletypeattribute) {
        this.tupletypeattributes.add(tupletypeattribute);
    }

}