





import java.util.List;
import java.util.ArrayList;

public class sparqlas_DataExactCardinality extends ClassExpression {

    private int cardinality;



    public sparqlas_DataExactCardinality(
        int cardinality    ) {
        super(
        );
        this.cardinality = cardinality;
    }


    public int getCardinality() {
        return cardinality;
    }

    public void setCardinality(int cardinality) {
        this.cardinality = cardinality;
    }


}