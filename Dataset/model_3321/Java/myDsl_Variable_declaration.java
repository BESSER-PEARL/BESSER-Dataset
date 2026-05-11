





import java.util.List;
import java.util.ArrayList;

public class myDsl_Variable_declaration  {

    private String modifiersVariable;





    private myDsl_Field_declaration mydsl_field_declaration;


    public myDsl_Variable_declaration(
        String modifiersVariable    ) {
        this.modifiersVariable = modifiersVariable;
    }


    public String getModifiersvariable() {
        return modifiersVariable;
    }

    public void setModifiersvariable(String modifiersVariable) {
        this.modifiersVariable = modifiersVariable;
    }

    public myDsl_Field_declaration getMydsl_field_declaration() {
        return mydsl_field_declaration;
    }

    public void setMydsl_field_declaration(myDsl_Field_declaration mydsl_field_declaration) {
        this.mydsl_field_declaration = mydsl_field_declaration;
    }

}