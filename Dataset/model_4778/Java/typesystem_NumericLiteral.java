





import java.util.List;
import java.util.ArrayList;

public class typesystem_NumericLiteral extends Literal {

    private String modifier;





    private typesystem_Unit typesystem_unit;


    public typesystem_NumericLiteral(
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

    public typesystem_Unit getTypesystem_unit() {
        return typesystem_unit;
    }

    public void setTypesystem_unit(typesystem_Unit typesystem_unit) {
        this.typesystem_unit = typesystem_unit;
    }

}