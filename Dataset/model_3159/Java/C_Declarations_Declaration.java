





import java.util.List;
import java.util.ArrayList;

public class C_Declarations_Declaration extends NamedElement {

    private String modifier;



    public C_Declarations_Declaration(
        String modifier    ) {
        super(
        );
        this.modifier = modifier;
    }


    public String getModifier() {
        return modifier;
    }

    public void setModifier(String modifier) {
        this.modifier = modifier;
    }


}