





import java.util.List;
import java.util.ArrayList;

public class myDsl_struct_declaration  {






    private myDsl_struct_declaration_list mydsl_struct_declaration_list;




    private myDsl_struct_declarator_list mydsl_struct_declarator_list;




    private myDsl_specifier_qualifier_list mydsl_specifier_qualifier_list;




    private myDsl_struct_declaration_listR mydsl_struct_declaration_listr;


    public myDsl_struct_declaration(
    ) {
    }



    public myDsl_struct_declaration_list getMydsl_struct_declaration_list() {
        return mydsl_struct_declaration_list;
    }

    public void setMydsl_struct_declaration_list(myDsl_struct_declaration_list mydsl_struct_declaration_list) {
        this.mydsl_struct_declaration_list = mydsl_struct_declaration_list;
    }
    public myDsl_struct_declarator_list getMydsl_struct_declarator_list() {
        return mydsl_struct_declarator_list;
    }

    public void setMydsl_struct_declarator_list(myDsl_struct_declarator_list mydsl_struct_declarator_list) {
        this.mydsl_struct_declarator_list = mydsl_struct_declarator_list;
    }
    public myDsl_specifier_qualifier_list getMydsl_specifier_qualifier_list() {
        return mydsl_specifier_qualifier_list;
    }

    public void setMydsl_specifier_qualifier_list(myDsl_specifier_qualifier_list mydsl_specifier_qualifier_list) {
        this.mydsl_specifier_qualifier_list = mydsl_specifier_qualifier_list;
    }
    public myDsl_struct_declaration_listR getMydsl_struct_declaration_listr() {
        return mydsl_struct_declaration_listr;
    }

    public void setMydsl_struct_declaration_listr(myDsl_struct_declaration_listR mydsl_struct_declaration_listr) {
        this.mydsl_struct_declaration_listr = mydsl_struct_declaration_listr;
    }

}