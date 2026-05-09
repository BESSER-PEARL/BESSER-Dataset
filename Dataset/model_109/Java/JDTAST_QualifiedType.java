





import java.util.List;
import java.util.ArrayList;

public class JDTAST_QualifiedType extends Type {






    private JDTAST_Type jdtast_type;




    private JDTAST_SimpleName jdtast_simplename;


    public JDTAST_QualifiedType(
    ) {
        super(
        );
    }



    public JDTAST_Type getJdtast_type() {
        return jdtast_type;
    }

    public void setJdtast_type(JDTAST_Type jdtast_type) {
        this.jdtast_type = jdtast_type;
    }
    public JDTAST_SimpleName getJdtast_simplename() {
        return jdtast_simplename;
    }

    public void setJdtast_simplename(JDTAST_SimpleName jdtast_simplename) {
        this.jdtast_simplename = jdtast_simplename;
    }

}