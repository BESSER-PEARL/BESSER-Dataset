





import java.util.List;
import java.util.ArrayList;

public class C_CompilationDirectiveDeclarations_Define extends SimpleDirectiveDeclaration {

    private String value;



    public C_CompilationDirectiveDeclarations_Define(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}