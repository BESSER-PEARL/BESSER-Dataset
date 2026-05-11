





import java.util.List;
import java.util.ArrayList;

public class myDsl_type_qualifier  {

    private String namez;





    private myDsl_declaration_specifiers mydsl_declaration_specifiers;


    public myDsl_type_qualifier(
        String namez    ) {
        this.namez = namez;
    }


    public String getNamez() {
        return namez;
    }

    public void setNamez(String namez) {
        this.namez = namez;
    }

    public myDsl_declaration_specifiers getMydsl_declaration_specifiers() {
        return mydsl_declaration_specifiers;
    }

    public void setMydsl_declaration_specifiers(myDsl_declaration_specifiers mydsl_declaration_specifiers) {
        this.mydsl_declaration_specifiers = mydsl_declaration_specifiers;
    }

}