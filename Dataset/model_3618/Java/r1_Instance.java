





import java.util.List;
import java.util.ArrayList;

public class r1_Instance extends Expression {

    private String classType;



    public r1_Instance(
        String classType    ) {
        super(
        );
        this.classType = classType;
    }


    public String getClasstype() {
        return classType;
    }

    public void setClasstype(String classType) {
        this.classType = classType;
    }


}