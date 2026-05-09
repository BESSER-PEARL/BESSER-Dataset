





import java.util.List;
import java.util.ArrayList;

public class OCL_OclType extends OclExpression {

    private String name;





    private CollectionType collectiontype;




    private TupleTypeAttribute tupletypeattribute;


    public OCL_OclType(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public CollectionType getCollectiontype() {
        return collectiontype;
    }

    public void setCollectiontype(CollectionType collectiontype) {
        this.collectiontype = collectiontype;
    }
    public TupleTypeAttribute getTupletypeattribute() {
        return tupletypeattribute;
    }

    public void setTupletypeattribute(TupleTypeAttribute tupletypeattribute) {
        this.tupletypeattribute = tupletypeattribute;
    }

}