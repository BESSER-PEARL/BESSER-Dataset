





import java.util.List;
import java.util.ArrayList;

public class sml_SmlEEnumLiteral  {

    private String name;





    private sml_EnumValue sml_enumvalue;


    public sml_SmlEEnumLiteral(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sml_EnumValue getSml_enumvalue() {
        return sml_enumvalue;
    }

    public void setSml_enumvalue(sml_EnumValue sml_enumvalue) {
        this.sml_enumvalue = sml_enumvalue;
    }

}