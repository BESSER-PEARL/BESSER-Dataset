





import java.util.List;
import java.util.ArrayList;

public class robochart_VectorType extends Type {

    private int size;





    private robochart_Type robochart_type;


    public robochart_VectorType(
        int size    ) {
        super(
        );
        this.size = size;
    }


    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }

    public robochart_Type getRobochart_type() {
        return robochart_type;
    }

    public void setRobochart_type(robochart_Type robochart_type) {
        this.robochart_type = robochart_type;
    }

}