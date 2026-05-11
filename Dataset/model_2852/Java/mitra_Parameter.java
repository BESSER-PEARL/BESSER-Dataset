





import java.util.List;
import java.util.ArrayList;

public class mitra_Parameter  {

    private String modifier;





    private mitra_TypedVarDeclaration mitra_typedvardeclaration;


    public mitra_Parameter(
        String modifier    ) {
        this.modifier = modifier;
    }


    public String getModifier() {
        return modifier;
    }

    public void setModifier(String modifier) {
        this.modifier = modifier;
    }

    public mitra_TypedVarDeclaration getMitra_typedvardeclaration() {
        return mitra_typedvardeclaration;
    }

    public void setMitra_typedvardeclaration(mitra_TypedVarDeclaration mitra_typedvardeclaration) {
        this.mitra_typedvardeclaration = mitra_typedvardeclaration;
    }

}