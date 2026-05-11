





import java.util.List;
import java.util.ArrayList;

public class myDsl_struct_declaration  {






    private myDsl_struct_declaration_list mydsl_struct_declaration_list;




    private myDsl_static_assert_declaration mydsl_static_assert_declaration;


    public myDsl_struct_declaration(
    ) {
    }



    public myDsl_struct_declaration_list getMydsl_struct_declaration_list() {
        return mydsl_struct_declaration_list;
    }

    public void setMydsl_struct_declaration_list(myDsl_struct_declaration_list mydsl_struct_declaration_list) {
        this.mydsl_struct_declaration_list = mydsl_struct_declaration_list;
    }
    public myDsl_static_assert_declaration getMydsl_static_assert_declaration() {
        return mydsl_static_assert_declaration;
    }

    public void setMydsl_static_assert_declaration(myDsl_static_assert_declaration mydsl_static_assert_declaration) {
        this.mydsl_static_assert_declaration = mydsl_static_assert_declaration;
    }

}