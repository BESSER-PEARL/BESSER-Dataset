





import java.util.List;
import java.util.ArrayList;

public class simpleocl_TupleType extends OclType {






    private List<simpleocl_TupleTypeAttribute> simpleocl_tupletypeattributes;




    private simpleocl_TupleTypeAttribute simpleocl_tupletypeattribute;


    public simpleocl_TupleType(
    ) {
        super(
        );
        this.simpleocl_tupletypeattributes = new ArrayList<>();
    }

    public simpleocl_TupleType(
        ArrayList<simpleocl_TupleTypeAttribute> simpleocl_tupletypeattributes    ) {
        this.simpleocl_tupletypeattributes = simpleocl_tupletypeattributes;
    }


    public List<simpleocl_TupleTypeAttribute> getSimpleocl_tupletypeattributes() {
        return simpleocl_tupletypeattributes;
    }

    public void addSimpleocl_tupletypeattribute(Simpleocl_tupletypeattribute simpleocl_tupletypeattribute) {
        this.simpleocl_tupletypeattributes.add(simpleocl_tupletypeattribute);
    }
    public simpleocl_TupleTypeAttribute getSimpleocl_tupletypeattribute() {
        return simpleocl_tupletypeattribute;
    }

    public void setSimpleocl_tupletypeattribute(simpleocl_TupleTypeAttribute simpleocl_tupletypeattribute) {
        this.simpleocl_tupletypeattribute = simpleocl_tupletypeattribute;
    }

}