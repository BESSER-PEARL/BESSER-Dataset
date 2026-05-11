





import java.util.List;
import java.util.ArrayList;

public class camel_provider_Attribute  {

    private String name;
    private String unitType;





    private ValueType valuetype;




    private SingleValue singlevalue;


    public camel_provider_Attribute(
        String name,        String unitType    ) {
        this.name = name;
        this.unitType = unitType;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUnittype() {
        return unitType;
    }

    public void setUnittype(String unitType) {
        this.unitType = unitType;
    }

    public ValueType getValuetype() {
        return valuetype;
    }

    public void setValuetype(ValueType valuetype) {
        this.valuetype = valuetype;
    }
    public SingleValue getSinglevalue() {
        return singlevalue;
    }

    public void setSinglevalue(SingleValue singlevalue) {
        this.singlevalue = singlevalue;
    }

}