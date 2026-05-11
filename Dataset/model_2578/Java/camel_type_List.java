





import java.util.List;
import java.util.ArrayList;

public class camel_type_List extends ValueType {

    private String primitiveType;





    private List<SingleValue> singlevalues;


    public camel_type_List(
        String primitiveType    ) {
        super(
        );
        this.primitiveType = primitiveType;
        this.singlevalues = new ArrayList<>();
    }

    public camel_type_List(
        String primitiveType        ArrayList<SingleValue> singlevalues    ) {
        this.primitiveType = primitiveType;
        this.singlevalues = singlevalues;
    }

    public String getPrimitivetype() {
        return primitiveType;
    }

    public void setPrimitivetype(String primitiveType) {
        this.primitiveType = primitiveType;
    }

    public List<SingleValue> getSinglevalues() {
        return singlevalues;
    }

    public void addSinglevalue(Singlevalue singlevalue) {
        this.singlevalues.add(singlevalue);
    }

}