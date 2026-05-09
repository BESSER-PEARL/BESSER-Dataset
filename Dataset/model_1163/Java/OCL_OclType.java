





import java.util.List;
import java.util.ArrayList;

public class OCL_OclType extends OclExpression {

    private String name;





    private MapType maptype;




    private MapType maptype;




    private Attribute attribute;




    private VariableDeclaration variabledeclaration;




    private CollectionType collectiontype;




    private Operation operation;




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

    public MapType getMaptype() {
        return maptype;
    }

    public void setMaptype(MapType maptype) {
        this.maptype = maptype;
    }
    public MapType getMaptype() {
        return maptype;
    }

    public void setMaptype(MapType maptype) {
        this.maptype = maptype;
    }
    public Attribute getAttribute() {
        return attribute;
    }

    public void setAttribute(Attribute attribute) {
        this.attribute = attribute;
    }
    public VariableDeclaration getVariabledeclaration() {
        return variabledeclaration;
    }

    public void setVariabledeclaration(VariableDeclaration variabledeclaration) {
        this.variabledeclaration = variabledeclaration;
    }
    public CollectionType getCollectiontype() {
        return collectiontype;
    }

    public void setCollectiontype(CollectionType collectiontype) {
        this.collectiontype = collectiontype;
    }
    public Operation getOperation() {
        return operation;
    }

    public void setOperation(Operation operation) {
        this.operation = operation;
    }
    public TupleTypeAttribute getTupletypeattribute() {
        return tupletypeattribute;
    }

    public void setTupletypeattribute(TupleTypeAttribute tupletypeattribute) {
        this.tupletypeattribute = tupletypeattribute;
    }

}