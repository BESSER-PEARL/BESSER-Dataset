





import java.util.List;
import java.util.ArrayList;

public class C_Main_Function extends Element {

    private String modifier;
    private String functionModifier;



    public C_Main_Function(
        String modifier,        String functionModifier    ) {
        super(
        );
        this.modifier = modifier;
        this.functionModifier = functionModifier;
    }


    public String getModifier() {
        return modifier;
    }

    public void setModifier(String modifier) {
        this.modifier = modifier;
    }
    public String getFunctionmodifier() {
        return functionModifier;
    }

    public void setFunctionmodifier(String functionModifier) {
        this.functionModifier = functionModifier;
    }


}