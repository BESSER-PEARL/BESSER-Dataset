





import java.util.List;
import java.util.ArrayList;

public class JDTAST_QualifiedName extends Name {






    private JDTAST_Name jdtast_name;




    private JDTAST_SimpleName jdtast_simplename;


    public JDTAST_QualifiedName(
    ) {
        super(
        );
    }



    public JDTAST_Name getJdtast_name() {
        return jdtast_name;
    }

    public void setJdtast_name(JDTAST_Name jdtast_name) {
        this.jdtast_name = jdtast_name;
    }
    public JDTAST_SimpleName getJdtast_simplename() {
        return jdtast_simplename;
    }

    public void setJdtast_simplename(JDTAST_SimpleName jdtast_simplename) {
        this.jdtast_simplename = jdtast_simplename;
    }

}