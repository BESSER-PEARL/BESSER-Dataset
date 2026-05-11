





import java.util.List;
import java.util.ArrayList;

public class typedef_EnumLiteral  {

    private String value;
    private String name;





    private typedef_TDDocumentation typedef_tddocumentation;




    private typedef_EnumVal typedef_enumval;


    public typedef_EnumLiteral(
        String value,        String name    ) {
        this.value = value;
        this.name = name;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public typedef_TDDocumentation getTypedef_tddocumentation() {
        return typedef_tddocumentation;
    }

    public void setTypedef_tddocumentation(typedef_TDDocumentation typedef_tddocumentation) {
        this.typedef_tddocumentation = typedef_tddocumentation;
    }
    public typedef_EnumVal getTypedef_enumval() {
        return typedef_enumval;
    }

    public void setTypedef_enumval(typedef_EnumVal typedef_enumval) {
        this.typedef_enumval = typedef_enumval;
    }

}