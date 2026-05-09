





import java.util.List;
import java.util.ArrayList;

public class henshin_AttributeCondition extends NamedElement {

    private String conditionText;



    public henshin_AttributeCondition(
        String conditionText    ) {
        super(
        );
        this.conditionText = conditionText;
    }


    public String getConditiontext() {
        return conditionText;
    }

    public void setConditiontext(String conditionText) {
        this.conditionText = conditionText;
    }


}