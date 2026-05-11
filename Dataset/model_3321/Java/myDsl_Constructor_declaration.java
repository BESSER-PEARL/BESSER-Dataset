





import java.util.List;
import java.util.ArrayList;

public class myDsl_Constructor_declaration  {

    private String lParen;
    private String rparent;
    private String nameConstructor;
    private String modifiersConstructor;





    private myDsl_Field_declaration mydsl_field_declaration;


    public myDsl_Constructor_declaration(
        String lParen,        String rparent,        String nameConstructor,        String modifiersConstructor    ) {
        this.lParen = lParen;
        this.rparent = rparent;
        this.nameConstructor = nameConstructor;
        this.modifiersConstructor = modifiersConstructor;
    }


    public String getLparen() {
        return lParen;
    }

    public void setLparen(String lParen) {
        this.lParen = lParen;
    }
    public String getRparent() {
        return rparent;
    }

    public void setRparent(String rparent) {
        this.rparent = rparent;
    }
    public String getNameconstructor() {
        return nameConstructor;
    }

    public void setNameconstructor(String nameConstructor) {
        this.nameConstructor = nameConstructor;
    }
    public String getModifiersconstructor() {
        return modifiersConstructor;
    }

    public void setModifiersconstructor(String modifiersConstructor) {
        this.modifiersConstructor = modifiersConstructor;
    }

    public myDsl_Field_declaration getMydsl_field_declaration() {
        return mydsl_field_declaration;
    }

    public void setMydsl_field_declaration(myDsl_Field_declaration mydsl_field_declaration) {
        this.mydsl_field_declaration = mydsl_field_declaration;
    }

}