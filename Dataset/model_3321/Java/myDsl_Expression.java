





import java.util.List;
import java.util.ArrayList;

public class myDsl_Expression  {

    private String name;
    private String super;
    private String this;
    private String null;





    private myDsl_Variable_initializer mydsl_variable_initializer;


    public myDsl_Expression(
        String name,        String super,        String this,        String null    ) {
        this.name = name;
        this.super = super;
        this.this = this;
        this.null = null;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSuper() {
        return super;
    }

    public void setSuper(String super) {
        this.super = super;
    }
    public String getThis() {
        return this;
    }

    public void setThis(String this) {
        this.this = this;
    }
    public String getNull() {
        return null;
    }

    public void setNull(String null) {
        this.null = null;
    }

    public myDsl_Variable_initializer getMydsl_variable_initializer() {
        return mydsl_variable_initializer;
    }

    public void setMydsl_variable_initializer(myDsl_Variable_initializer mydsl_variable_initializer) {
        this.mydsl_variable_initializer = mydsl_variable_initializer;
    }

}