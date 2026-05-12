





import java.util.List;
import java.util.ArrayList;

public class SQLDML_StringValueExp extends ValueExp {

    private String aValue;



    public SQLDML_StringValueExp(
        String aValue    ) {
        super(
        );
        this.aValue = aValue;
    }


    public String getAvalue() {
        return aValue;
    }

    public void setAvalue(String aValue) {
        this.aValue = aValue;
    }


}