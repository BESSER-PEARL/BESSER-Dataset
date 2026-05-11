





import java.util.List;
import java.util.ArrayList;

public class robochart_Variable extends TypedNamedElement, Member, NamedExpression {

    private String modifier;



    public robochart_Variable(
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