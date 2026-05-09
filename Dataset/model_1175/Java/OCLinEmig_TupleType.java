





import java.util.List;
import java.util.ArrayList;

public class OCLinEmig_TupleType extends OclType {






    private OCLinEmig_TupleTypeAttribute oclinemig_tupletypeattribute;




    private List<OCLinEmig_TupleTypeAttribute> oclinemig_tupletypeattributes;


    public OCLinEmig_TupleType(
    ) {
        super(
        );
        this.oclinemig_tupletypeattributes = new ArrayList<>();
    }

    public OCLinEmig_TupleType(
        ArrayList<OCLinEmig_TupleTypeAttribute> oclinemig_tupletypeattributes    ) {
        this.oclinemig_tupletypeattributes = oclinemig_tupletypeattributes;
    }


    public OCLinEmig_TupleTypeAttribute getOclinemig_tupletypeattribute() {
        return oclinemig_tupletypeattribute;
    }

    public void setOclinemig_tupletypeattribute(OCLinEmig_TupleTypeAttribute oclinemig_tupletypeattribute) {
        this.oclinemig_tupletypeattribute = oclinemig_tupletypeattribute;
    }
    public List<OCLinEmig_TupleTypeAttribute> getOclinemig_tupletypeattributes() {
        return oclinemig_tupletypeattributes;
    }

    public void addOclinemig_tupletypeattribute(Oclinemig_tupletypeattribute oclinemig_tupletypeattribute) {
        this.oclinemig_tupletypeattributes.add(oclinemig_tupletypeattribute);
    }

}