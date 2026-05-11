





import java.util.List;
import java.util.ArrayList;

public class myDsl_declaration  {






    private myDsl_static_assert_declaration mydsl_static_assert_declaration;




    private myDsl_init_declarator_list mydsl_init_declarator_list;


    public myDsl_declaration(
    ) {
    }



    public myDsl_static_assert_declaration getMydsl_static_assert_declaration() {
        return mydsl_static_assert_declaration;
    }

    public void setMydsl_static_assert_declaration(myDsl_static_assert_declaration mydsl_static_assert_declaration) {
        this.mydsl_static_assert_declaration = mydsl_static_assert_declaration;
    }
    public myDsl_init_declarator_list getMydsl_init_declarator_list() {
        return mydsl_init_declarator_list;
    }

    public void setMydsl_init_declarator_list(myDsl_init_declarator_list mydsl_init_declarator_list) {
        this.mydsl_init_declarator_list = mydsl_init_declarator_list;
    }

}