





import java.util.List;
import java.util.ArrayList;

public class smalluml_Enumeration extends NamedElement {

    private String enumValue;



    public smalluml_Enumeration(
        String enumValue    ) {
        super(
        );
        this.enumValue = enumValue;
    }


    public String getEnumvalue() {
        return enumValue;
    }

    public void setEnumvalue(String enumValue) {
        this.enumValue = enumValue;
    }


}