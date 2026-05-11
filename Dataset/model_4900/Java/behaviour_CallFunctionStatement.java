





import java.util.List;
import java.util.ArrayList;

public class behaviour_CallFunctionStatement extends Statement {

    private String nameFunc;



    public behaviour_CallFunctionStatement(
        String nameFunc    ) {
        super(
        );
        this.nameFunc = nameFunc;
    }


    public String getNamefunc() {
        return nameFunc;
    }

    public void setNamefunc(String nameFunc) {
        this.nameFunc = nameFunc;
    }


}