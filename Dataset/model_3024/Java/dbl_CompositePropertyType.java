





import java.util.List;
import java.util.ArrayList;

public class dbl_CompositePropertyType extends StructuredPropertyType {

    private boolean list;



    public dbl_CompositePropertyType(
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