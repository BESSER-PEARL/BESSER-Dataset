





import java.util.List;
import java.util.ArrayList;

public class arduino_Read extends Function {

    private String returnValue;
    private String name;



    public arduino_Read(
        String returnValue,        String name    ) {
        super(
        );
        this.returnValue = returnValue;
        this.name = name;
    }


    public String getReturnvalue() {
        return returnValue;
    }

    public void setReturnvalue(String returnValue) {
        this.returnValue = returnValue;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}