





import java.util.List;
import java.util.ArrayList;

public class HALL_Conditions_Let extends PreConditionMessageExpressionElement {

    private String namevar;



    public HALL_Conditions_Let(
        String namevar    ) {
        super(
        );
        this.namevar = namevar;
    }


    public String getNamevar() {
        return namevar;
    }

    public void setNamevar(String namevar) {
        this.namevar = namevar;
    }


}