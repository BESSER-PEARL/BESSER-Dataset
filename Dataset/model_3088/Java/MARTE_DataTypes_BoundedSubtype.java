





import java.util.List;
import java.util.ArrayList;

public class MARTE_DataTypes_BoundedSubtype  {

    private boolean isMinOpen;
    private String minValue;
    private String maxValue;
    private boolean isMaxOpen;





    private DataTypes_MARTE_DataType datatypes_marte_datatype;




    private DataTypes_MARTE_DataType datatypes_marte_datatype;


    public MARTE_DataTypes_BoundedSubtype(
        boolean isMinOpen,        String minValue,        String maxValue,        boolean isMaxOpen    ) {
        this.isMinOpen = isMinOpen;
        this.minValue = minValue;
        this.maxValue = maxValue;
        this.isMaxOpen = isMaxOpen;
    }


    public boolean getIsminopen() {
        return isMinOpen;
    }

    public void setIsminopen(boolean isMinOpen) {
        this.isMinOpen = isMinOpen;
    }
    public String getMinvalue() {
        return minValue;
    }

    public void setMinvalue(String minValue) {
        this.minValue = minValue;
    }
    public String getMaxvalue() {
        return maxValue;
    }

    public void setMaxvalue(String maxValue) {
        this.maxValue = maxValue;
    }
    public boolean getIsmaxopen() {
        return isMaxOpen;
    }

    public void setIsmaxopen(boolean isMaxOpen) {
        this.isMaxOpen = isMaxOpen;
    }

    public DataTypes_MARTE_DataType getDatatypes_marte_datatype() {
        return datatypes_marte_datatype;
    }

    public void setDatatypes_marte_datatype(DataTypes_MARTE_DataType datatypes_marte_datatype) {
        this.datatypes_marte_datatype = datatypes_marte_datatype;
    }
    public DataTypes_MARTE_DataType getDatatypes_marte_datatype() {
        return datatypes_marte_datatype;
    }

    public void setDatatypes_marte_datatype(DataTypes_MARTE_DataType datatypes_marte_datatype) {
        this.datatypes_marte_datatype = datatypes_marte_datatype;
    }

}