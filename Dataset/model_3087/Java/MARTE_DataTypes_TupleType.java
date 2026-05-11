





import java.util.List;
import java.util.ArrayList;

public class MARTE_DataTypes_TupleType  {






    private List<DataTypes_MARTE_Property> datatypes_marte_propertys;




    private DataTypes_MARTE_DataType datatypes_marte_datatype;


    public MARTE_DataTypes_TupleType(
    ) {
        this.datatypes_marte_propertys = new ArrayList<>();
    }

    public MARTE_DataTypes_TupleType(
        ArrayList<DataTypes_MARTE_Property> datatypes_marte_propertys    ) {
        this.datatypes_marte_propertys = datatypes_marte_propertys;
    }


    public List<DataTypes_MARTE_Property> getDatatypes_marte_propertys() {
        return datatypes_marte_propertys;
    }

    public void addDatatypes_marte_property(Datatypes_marte_property datatypes_marte_property) {
        this.datatypes_marte_propertys.add(datatypes_marte_property);
    }
    public DataTypes_MARTE_DataType getDatatypes_marte_datatype() {
        return datatypes_marte_datatype;
    }

    public void setDatatypes_marte_datatype(DataTypes_MARTE_DataType datatypes_marte_datatype) {
        this.datatypes_marte_datatype = datatypes_marte_datatype;
    }

}