





import java.util.List;
import java.util.ArrayList;

public class datatypes_Field  {

    private String measureUnit;
    private String name;
    private String description;





    private datatypes_DataType datatypes_datatype;




    private datatypes_CustomType datatypes_customtype;


    public datatypes_Field(
        String measureUnit,        String name,        String description    ) {
        this.measureUnit = measureUnit;
        this.name = name;
        this.description = description;
    }


    public String getMeasureunit() {
        return measureUnit;
    }

    public void setMeasureunit(String measureUnit) {
        this.measureUnit = measureUnit;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public datatypes_DataType getDatatypes_datatype() {
        return datatypes_datatype;
    }

    public void setDatatypes_datatype(datatypes_DataType datatypes_datatype) {
        this.datatypes_datatype = datatypes_datatype;
    }
    public datatypes_CustomType getDatatypes_customtype() {
        return datatypes_customtype;
    }

    public void setDatatypes_customtype(datatypes_CustomType datatypes_customtype) {
        this.datatypes_customtype = datatypes_customtype;
    }

}