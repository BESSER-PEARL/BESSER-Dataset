





import java.util.List;
import java.util.ArrayList;

public class cwm_relational_TdColumn extends Column {

    private int javaType;



    public cwm_relational_TdColumn(
        int javaType    ) {
        super(
        );
        this.javaType = javaType;
    }


    public int getJavatype() {
        return javaType;
    }

    public void setJavatype(int javaType) {
        this.javaType = javaType;
    }


}