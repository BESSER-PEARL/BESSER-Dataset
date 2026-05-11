





import java.util.List;
import java.util.ArrayList;

public class applauseDsl_TypeMapping extends PlatformMapping {

    private String simpleName;





    private applauseDsl_DataType applausedsl_datatype;


    public applauseDsl_TypeMapping(
        String simpleName    ) {
        super(
        );
        this.simpleName = simpleName;
    }


    public String getSimplename() {
        return simpleName;
    }

    public void setSimplename(String simpleName) {
        this.simpleName = simpleName;
    }

    public applauseDsl_DataType getApplausedsl_datatype() {
        return applausedsl_datatype;
    }

    public void setApplausedsl_datatype(applauseDsl_DataType applausedsl_datatype) {
        this.applausedsl_datatype = applausedsl_datatype;
    }

}