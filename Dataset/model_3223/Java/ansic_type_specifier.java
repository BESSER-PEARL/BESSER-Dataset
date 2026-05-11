





import java.util.List;
import java.util.ArrayList;

public class ansic_type_specifier  {

    private String type_name_str;





    private ansic_declaration_specifiers ansic_declaration_specifiers;


    public ansic_type_specifier(
        String type_name_str    ) {
        this.type_name_str = type_name_str;
    }


    public String getType_name_str() {
        return type_name_str;
    }

    public void setType_name_str(String type_name_str) {
        this.type_name_str = type_name_str;
    }

    public ansic_declaration_specifiers getAnsic_declaration_specifiers() {
        return ansic_declaration_specifiers;
    }

    public void setAnsic_declaration_specifiers(ansic_declaration_specifiers ansic_declaration_specifiers) {
        this.ansic_declaration_specifiers = ansic_declaration_specifiers;
    }

}