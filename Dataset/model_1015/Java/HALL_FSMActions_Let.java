





import java.util.List;
import java.util.ArrayList;

public class HALL_FSMActions_Let extends ActionExpressionElement {

    private String namevar;



    public HALL_FSMActions_Let(
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