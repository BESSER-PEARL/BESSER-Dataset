





import java.util.List;
import java.util.ArrayList;

public class uppaal_declarations_DataVariableDeclaration extends VariableDeclaration {

    private String prefix;



    public uppaal_declarations_DataVariableDeclaration(
        String prefix    ) {
        super(
        );
        this.prefix = prefix;
    }


    public String getPrefix() {
        return prefix;
    }

    public void setPrefix(String prefix) {
        this.prefix = prefix;
    }


}