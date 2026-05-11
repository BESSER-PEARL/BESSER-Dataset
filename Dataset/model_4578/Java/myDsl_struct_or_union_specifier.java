





import java.util.List;
import java.util.ArrayList;

public class myDsl_struct_or_union_specifier extends type_specifier {

    private String Struct_or_union;





    private myDsl_struct_declaration_list mydsl_struct_declaration_list;




    private myDsl_IDENTIFIER mydsl_identifier;


    public myDsl_struct_or_union_specifier(
        String Struct_or_union    ) {
        super(
        );
        this.Struct_or_union = Struct_or_union;
    }


    public String getStruct_or_union() {
        return Struct_or_union;
    }

    public void setStruct_or_union(String Struct_or_union) {
        this.Struct_or_union = Struct_or_union;
    }

    public myDsl_struct_declaration_list getMydsl_struct_declaration_list() {
        return mydsl_struct_declaration_list;
    }

    public void setMydsl_struct_declaration_list(myDsl_struct_declaration_list mydsl_struct_declaration_list) {
        this.mydsl_struct_declaration_list = mydsl_struct_declaration_list;
    }
    public myDsl_IDENTIFIER getMydsl_identifier() {
        return mydsl_identifier;
    }

    public void setMydsl_identifier(myDsl_IDENTIFIER mydsl_identifier) {
        this.mydsl_identifier = mydsl_identifier;
    }

}