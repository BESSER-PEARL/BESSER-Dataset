





import java.util.List;
import java.util.ArrayList;

public class myDsl_Method_declaration  {

    private String lParen;
    private String nameMethod;
    private String modifiersMethod;
    private String rparent;
    private String debug;





    private myDsl_Field_declaration mydsl_field_declaration;


    public myDsl_Method_declaration(
        String lParen,        String nameMethod,        String modifiersMethod,        String rparent,        String debug    ) {
        this.lParen = lParen;
        this.nameMethod = nameMethod;
        this.modifiersMethod = modifiersMethod;
        this.rparent = rparent;
        this.debug = debug;
    }


    public String getLparen() {
        return lParen;
    }

    public void setLparen(String lParen) {
        this.lParen = lParen;
    }
    public String getNamemethod() {
        return nameMethod;
    }

    public void setNamemethod(String nameMethod) {
        this.nameMethod = nameMethod;
    }
    public String getModifiersmethod() {
        return modifiersMethod;
    }

    public void setModifiersmethod(String modifiersMethod) {
        this.modifiersMethod = modifiersMethod;
    }
    public String getRparent() {
        return rparent;
    }

    public void setRparent(String rparent) {
        this.rparent = rparent;
    }
    public String getDebug() {
        return debug;
    }

    public void setDebug(String debug) {
        this.debug = debug;
    }

    public myDsl_Field_declaration getMydsl_field_declaration() {
        return mydsl_field_declaration;
    }

    public void setMydsl_field_declaration(myDsl_Field_declaration mydsl_field_declaration) {
        this.mydsl_field_declaration = mydsl_field_declaration;
    }

}