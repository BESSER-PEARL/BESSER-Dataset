





import java.util.List;
import java.util.ArrayList;

public class datatypes_Field  {

    private String name;
    private boolean many;





    private datatypes_DataType datatypes_datatype;




    private datatypes_ComplexType datatypes_complextype;


    public datatypes_Field(
        String name,        boolean many    ) {
        this.name = name;
        this.many = many;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getMany() {
        return many;
    }

    public void setMany(boolean many) {
        this.many = many;
    }

    public datatypes_DataType getDatatypes_datatype() {
        return datatypes_datatype;
    }

    public void setDatatypes_datatype(datatypes_DataType datatypes_datatype) {
        this.datatypes_datatype = datatypes_datatype;
    }
    public datatypes_ComplexType getDatatypes_complextype() {
        return datatypes_complextype;
    }

    public void setDatatypes_complextype(datatypes_ComplexType datatypes_complextype) {
        this.datatypes_complextype = datatypes_complextype;
    }

}