





import java.util.List;
import java.util.ArrayList;

public class typesystem_TensorType extends ArrayType {

    private boolean vector;
    private boolean matrix;



    public typesystem_TensorType(
        boolean vector,        boolean matrix    ) {
        super(
        );
        this.vector = vector;
        this.matrix = matrix;
    }


    public boolean getVector() {
        return vector;
    }

    public void setVector(boolean vector) {
        this.vector = vector;
    }
    public boolean getMatrix() {
        return matrix;
    }

    public void setMatrix(boolean matrix) {
        this.matrix = matrix;
    }


}