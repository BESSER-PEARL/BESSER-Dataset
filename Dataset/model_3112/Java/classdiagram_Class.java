





import java.util.List;
import java.util.ArrayList;

public class classdiagram_Class extends AttributeValue {

    private String name;
    private boolean is_persistent;



    public classdiagram_Class(
        String name,        boolean is_persistent    ) {
        super(
        );
        this.name = name;
        this.is_persistent = is_persistent;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIs_persistent() {
        return is_persistent;
    }

    public void setIs_persistent(boolean is_persistent) {
        this.is_persistent = is_persistent;
    }


}