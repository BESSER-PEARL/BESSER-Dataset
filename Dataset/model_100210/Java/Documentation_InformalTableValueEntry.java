





import java.util.List;
import java.util.ArrayList;

public class Documentation_InformalTableValueEntry  {

    private String value;





    private Documentation_InformalTableValueRow documentation_informaltablevaluerow;


    public Documentation_InformalTableValueEntry(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public Documentation_InformalTableValueRow getDocumentation_informaltablevaluerow() {
        return documentation_informaltablevaluerow;
    }

    public void setDocumentation_informaltablevaluerow(Documentation_InformalTableValueRow documentation_informaltablevaluerow) {
        this.documentation_informaltablevaluerow = documentation_informaltablevaluerow;
    }

}