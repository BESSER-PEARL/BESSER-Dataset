





import java.util.List;
import java.util.ArrayList;

public class go_CallFunc extends Greeting, Atrib_Aux {

    private String nameFunc;



    public go_CallFunc(
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