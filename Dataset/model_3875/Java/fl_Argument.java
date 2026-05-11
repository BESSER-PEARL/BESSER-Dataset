





import java.util.List;
import java.util.ArrayList;

public class fl_Argument  {

    private String name;





    private fl_Function fl_function;


    public fl_Argument(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fl_Function getFl_function() {
        return fl_function;
    }

    public void setFl_function(fl_Function fl_function) {
        this.fl_function = fl_function;
    }

}