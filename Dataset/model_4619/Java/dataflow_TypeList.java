





import java.util.List;
import java.util.ArrayList;

public class dataflow_TypeList extends Type {

    private int elements;





    private dataflow_Type dataflow_type;


    public dataflow_TypeList(
        int elements    ) {
        super(
        );
        this.elements = elements;
    }


    public int getElements() {
        return elements;
    }

    public void setElements(int elements) {
        this.elements = elements;
    }

    public dataflow_Type getDataflow_type() {
        return dataflow_type;
    }

    public void setDataflow_type(dataflow_Type dataflow_type) {
        this.dataflow_type = dataflow_type;
    }

}