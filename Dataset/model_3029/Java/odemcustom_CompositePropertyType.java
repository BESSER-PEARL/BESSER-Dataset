





import java.util.List;
import java.util.ArrayList;

public class odemcustom_CompositePropertyType extends StructuredPropertyType {

    private boolean list;



    public odemcustom_CompositePropertyType(
        boolean list    ) {
        super(
        );
        this.list = list;
    }


    public boolean getList() {
        return list;
    }

    public void setList(boolean list) {
        this.list = list;
    }


}