





import java.util.List;
import java.util.ArrayList;

public class HALL_FSMConditions_Let extends PreConditionExpressionElement {

    private String namevar;



    public HALL_FSMConditions_Let(
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