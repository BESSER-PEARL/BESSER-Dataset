





import java.util.List;
import java.util.ArrayList;

public class source_Attribute  {

    private String name;
    private boolean is_primary;





    private source_Class source_class;




    private source_Class source_class;


    public source_Attribute(
        String name,        boolean is_primary    ) {
        this.name = name;
        this.is_primary = is_primary;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIs_primary() {
        return is_primary;
    }

    public void setIs_primary(boolean is_primary) {
        this.is_primary = is_primary;
    }

    public source_Class getSource_class() {
        return source_class;
    }

    public void setSource_class(source_Class source_class) {
        this.source_class = source_class;
    }
    public source_Class getSource_class() {
        return source_class;
    }

    public void setSource_class(source_Class source_class) {
        this.source_class = source_class;
    }

}