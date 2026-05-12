





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_datatypes_ArrayDataType extends CollectionDataType {

    private int maxCardinality;



    public sqlmodel_datatypes_ArrayDataType(
        int maxCardinality    ) {
        super(
        );
        this.maxCardinality = maxCardinality;
    }


    public int getMaxcardinality() {
        return maxCardinality;
    }

    public void setMaxcardinality(int maxCardinality) {
        this.maxCardinality = maxCardinality;
    }


}