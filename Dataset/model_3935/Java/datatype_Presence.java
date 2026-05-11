





import java.util.List;
import java.util.ArrayList;

public class datatype_Presence  {

    private boolean mandatory;





    private datatype_Property datatype_property;


    public datatype_Presence(
        boolean mandatory    ) {
        this.mandatory = mandatory;
    }


    public boolean getMandatory() {
        return mandatory;
    }

    public void setMandatory(boolean mandatory) {
        this.mandatory = mandatory;
    }

    public datatype_Property getDatatype_property() {
        return datatype_property;
    }

    public void setDatatype_property(datatype_Property datatype_property) {
        this.datatype_property = datatype_property;
    }

}