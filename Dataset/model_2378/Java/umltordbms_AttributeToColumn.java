





import java.util.List;
import java.util.ArrayList;

public class umltordbms_AttributeToColumn extends FromAttribute, ToColumn {






    private umltordbms_PrimitiveToName umltordbms_primitivetoname;




    private umltordbms_FromAttribute umltordbms_fromattribute;


    public umltordbms_AttributeToColumn(
    ) {
        super(
        );
    }



    public umltordbms_PrimitiveToName getUmltordbms_primitivetoname() {
        return umltordbms_primitivetoname;
    }

    public void setUmltordbms_primitivetoname(umltordbms_PrimitiveToName umltordbms_primitivetoname) {
        this.umltordbms_primitivetoname = umltordbms_primitivetoname;
    }
    public umltordbms_FromAttribute getUmltordbms_fromattribute() {
        return umltordbms_fromattribute;
    }

    public void setUmltordbms_fromattribute(umltordbms_FromAttribute umltordbms_fromattribute) {
        this.umltordbms_fromattribute = umltordbms_fromattribute;
    }

}