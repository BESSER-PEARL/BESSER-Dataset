





import java.util.List;
import java.util.ArrayList;

public class source_Attribute  {

    private boolean is_primary;
    private String name;





    private source_PrimitiveDataType source_primitivedatatype;




    private source_Class source_class;




    private source_Class source_class;


    public source_Attribute(
        boolean is_primary,        String name    ) {
        this.is_primary = is_primary;
        this.name = name;
    }


    public boolean getIs_primary() {
        return is_primary;
    }

    public void setIs_primary(boolean is_primary) {
        this.is_primary = is_primary;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public source_PrimitiveDataType getSource_primitivedatatype() {
        return source_primitivedatatype;
    }

    public void setSource_primitivedatatype(source_PrimitiveDataType source_primitivedatatype) {
        this.source_primitivedatatype = source_primitivedatatype;
    }
    public source_Class getSource_class() {
        return source_class;
    }

    public void setSource_class(source_Class source_class) {
        this.source_class = source_class;
    }
    public source_Class getSource_class() {
        return source_class;
    }

    public void setSource_class(source_Class source_class) {
        this.source_class = source_class;
    }

}