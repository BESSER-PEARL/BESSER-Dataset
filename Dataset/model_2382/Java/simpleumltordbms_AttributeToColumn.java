





import java.util.List;
import java.util.ArrayList;

public class simpleumltordbms_AttributeToColumn extends ToColumn, FromAttribute {






    private simpleumltordbms_PrimitiveToName simpleumltordbms_primitivetoname;




    private simpleumltordbms_FromAttribute simpleumltordbms_fromattribute;


    public simpleumltordbms_AttributeToColumn(
    ) {
        super(
        );
    }



    public simpleumltordbms_PrimitiveToName getSimpleumltordbms_primitivetoname() {
        return simpleumltordbms_primitivetoname;
    }

    public void setSimpleumltordbms_primitivetoname(simpleumltordbms_PrimitiveToName simpleumltordbms_primitivetoname) {
        this.simpleumltordbms_primitivetoname = simpleumltordbms_primitivetoname;
    }
    public simpleumltordbms_FromAttribute getSimpleumltordbms_fromattribute() {
        return simpleumltordbms_fromattribute;
    }

    public void setSimpleumltordbms_fromattribute(simpleumltordbms_FromAttribute simpleumltordbms_fromattribute) {
        this.simpleumltordbms_fromattribute = simpleumltordbms_fromattribute;
    }

}