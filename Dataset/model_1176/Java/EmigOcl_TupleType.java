





import java.util.List;
import java.util.ArrayList;

public class EmigOcl_TupleType extends OclType {






    private List<EmigOcl_TupleTypeAttribute> emigocl_tupletypeattributes;




    private EmigOcl_TupleTypeAttribute emigocl_tupletypeattribute;


    public EmigOcl_TupleType(
    ) {
        super(
        );
        this.emigocl_tupletypeattributes = new ArrayList<>();
    }

    public EmigOcl_TupleType(
        ArrayList<EmigOcl_TupleTypeAttribute> emigocl_tupletypeattributes    ) {
        this.emigocl_tupletypeattributes = emigocl_tupletypeattributes;
    }


    public List<EmigOcl_TupleTypeAttribute> getEmigocl_tupletypeattributes() {
        return emigocl_tupletypeattributes;
    }

    public void addEmigocl_tupletypeattribute(Emigocl_tupletypeattribute emigocl_tupletypeattribute) {
        this.emigocl_tupletypeattributes.add(emigocl_tupletypeattribute);
    }
    public EmigOcl_TupleTypeAttribute getEmigocl_tupletypeattribute() {
        return emigocl_tupletypeattribute;
    }

    public void setEmigocl_tupletypeattribute(EmigOcl_TupleTypeAttribute emigocl_tupletypeattribute) {
        this.emigocl_tupletypeattribute = emigocl_tupletypeattribute;
    }

}