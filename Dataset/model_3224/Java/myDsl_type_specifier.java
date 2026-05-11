





import java.util.List;
import java.util.ArrayList;

public class myDsl_type_specifier  {

    private String type_name_str;





    private myDsl_declaration_specifiers mydsl_declaration_specifiers;


    public myDsl_type_specifier(
        String type_name_str    ) {
        this.type_name_str = type_name_str;
    }


    public String getType_name_str() {
        return type_name_str;
    }

    public void setType_name_str(String type_name_str) {
        this.type_name_str = type_name_str;
    }

    public myDsl_declaration_specifiers getMydsl_declaration_specifiers() {
        return mydsl_declaration_specifiers;
    }

    public void setMydsl_declaration_specifiers(myDsl_declaration_specifiers mydsl_declaration_specifiers) {
        this.mydsl_declaration_specifiers = mydsl_declaration_specifiers;
    }

}