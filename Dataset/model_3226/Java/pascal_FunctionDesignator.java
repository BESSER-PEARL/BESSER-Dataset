





import java.util.List;
import java.util.ArrayList;

public class pascal_FunctionDesignator  {

    private String name;





    private pascal_factor pascal_factor;


    public pascal_FunctionDesignator(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public pascal_factor getPascal_factor() {
        return pascal_factor;
    }

    public void setPascal_factor(pascal_factor pascal_factor) {
        this.pascal_factor = pascal_factor;
    }

}