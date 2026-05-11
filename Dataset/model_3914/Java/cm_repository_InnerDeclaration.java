





import java.util.List;
import java.util.ArrayList;

public class cm_repository_InnerDeclaration extends NamedElement {






    private DataType datatype;




    private CompositeDataType compositedatatype;


    public cm_repository_InnerDeclaration(
    ) {
        super(
        );
    }



    public DataType getDatatype() {
        return datatype;
    }

    public void setDatatype(DataType datatype) {
        this.datatype = datatype;
    }
    public CompositeDataType getCompositedatatype() {
        return compositedatatype;
    }

    public void setCompositedatatype(CompositeDataType compositedatatype) {
        this.compositedatatype = compositedatatype;
    }

}