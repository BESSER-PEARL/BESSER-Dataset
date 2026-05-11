





import java.util.List;
import java.util.ArrayList;

public class myDsl_Static_initializer  {

    private String static;





    private myDsl_Field_declaration mydsl_field_declaration;


    public myDsl_Static_initializer(
        String static    ) {
        this.static = static;
    }


    public String getStatic() {
        return static;
    }

    public void setStatic(String static) {
        this.static = static;
    }

    public myDsl_Field_declaration getMydsl_field_declaration() {
        return mydsl_field_declaration;
    }

    public void setMydsl_field_declaration(myDsl_Field_declaration mydsl_field_declaration) {
        this.mydsl_field_declaration = mydsl_field_declaration;
    }

}