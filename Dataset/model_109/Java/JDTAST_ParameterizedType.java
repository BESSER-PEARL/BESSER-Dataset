





import java.util.List;
import java.util.ArrayList;

public class JDTAST_ParameterizedType extends Type {






    private List<JDTAST_Type> jdtast_types;




    private JDTAST_Type jdtast_type;


    public JDTAST_ParameterizedType(
    ) {
        super(
        );
        this.jdtast_types = new ArrayList<>();
    }

    public JDTAST_ParameterizedType(
        ArrayList<JDTAST_Type> jdtast_types    ) {
        this.jdtast_types = jdtast_types;
    }


    public List<JDTAST_Type> getJdtast_types() {
        return jdtast_types;
    }

    public void addJdtast_type(Jdtast_type jdtast_type) {
        this.jdtast_types.add(jdtast_type);
    }
    public JDTAST_Type getJdtast_type() {
        return jdtast_type;
    }

    public void setJdtast_type(JDTAST_Type jdtast_type) {
        this.jdtast_type = jdtast_type;
    }

}