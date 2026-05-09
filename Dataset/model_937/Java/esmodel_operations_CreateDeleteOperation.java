





import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_CreateDeleteOperation extends AbstractOperation {

    private boolean delete;



    public esmodel_operations_CreateDeleteOperation(
        boolean delete    ) {
        super(
        );
        this.delete = delete;
    }


    public boolean getDelete() {
        return delete;
    }

    public void setDelete(boolean delete) {
        this.delete = delete;
    }


}