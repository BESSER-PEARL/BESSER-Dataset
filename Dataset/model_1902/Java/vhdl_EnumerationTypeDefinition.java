





import java.util.List;
import java.util.ArrayList;

public class vhdl_EnumerationTypeDefinition extends TypeDefinition {

    private String literal;



    public vhdl_EnumerationTypeDefinition(
        String literal    ) {
        super(
        );
        this.literal = literal;
    }


    public String getLiteral() {
        return literal;
    }

    public void setLiteral(String literal) {
        this.literal = literal;
    }


}