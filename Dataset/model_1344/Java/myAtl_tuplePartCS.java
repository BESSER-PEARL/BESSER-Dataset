





import java.util.List;
import java.util.ArrayList;

public class myAtl_tuplePartCS  {

    private String name;





    private myAtl_TypeExpCS myatl_typeexpcs;




    private myAtl_TupleTypeCS myatl_tupletypecs;


    public myAtl_tuplePartCS(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myAtl_TypeExpCS getMyatl_typeexpcs() {
        return myatl_typeexpcs;
    }

    public void setMyatl_typeexpcs(myAtl_TypeExpCS myatl_typeexpcs) {
        this.myatl_typeexpcs = myatl_typeexpcs;
    }
    public myAtl_TupleTypeCS getMyatl_tupletypecs() {
        return myatl_tupletypecs;
    }

    public void setMyatl_tupletypecs(myAtl_TupleTypeCS myatl_tupletypecs) {
        this.myatl_tupletypecs = myatl_tupletypecs;
    }

}