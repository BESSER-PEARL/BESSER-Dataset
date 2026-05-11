





import java.util.List;
import java.util.ArrayList;

public class myDsl_Statement_block  {

    private String lCurly;
    private String rCurly;





    private myDsl_Constructor_declaration mydsl_constructor_declaration;




    private myDsl_Static_initializer mydsl_static_initializer;




    private myDsl_Method_declaration mydsl_method_declaration;


    public myDsl_Statement_block(
        String lCurly,        String rCurly    ) {
        this.lCurly = lCurly;
        this.rCurly = rCurly;
    }


    public String getLcurly() {
        return lCurly;
    }

    public void setLcurly(String lCurly) {
        this.lCurly = lCurly;
    }
    public String getRcurly() {
        return rCurly;
    }

    public void setRcurly(String rCurly) {
        this.rCurly = rCurly;
    }

    public myDsl_Constructor_declaration getMydsl_constructor_declaration() {
        return mydsl_constructor_declaration;
    }

    public void setMydsl_constructor_declaration(myDsl_Constructor_declaration mydsl_constructor_declaration) {
        this.mydsl_constructor_declaration = mydsl_constructor_declaration;
    }
    public myDsl_Static_initializer getMydsl_static_initializer() {
        return mydsl_static_initializer;
    }

    public void setMydsl_static_initializer(myDsl_Static_initializer mydsl_static_initializer) {
        this.mydsl_static_initializer = mydsl_static_initializer;
    }
    public myDsl_Method_declaration getMydsl_method_declaration() {
        return mydsl_method_declaration;
    }

    public void setMydsl_method_declaration(myDsl_Method_declaration mydsl_method_declaration) {
        this.mydsl_method_declaration = mydsl_method_declaration;
    }

}