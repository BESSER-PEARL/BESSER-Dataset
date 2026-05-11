





import java.util.List;
import java.util.ArrayList;

public class applauseDsl_CustomView extends View {

    private String objclass;





    private applauseDsl_Parameter applausedsl_parameter;


    public applauseDsl_CustomView(
        String objclass    ) {
        super(
        );
        this.objclass = objclass;
    }


    public String getObjclass() {
        return objclass;
    }

    public void setObjclass(String objclass) {
        this.objclass = objclass;
    }

    public applauseDsl_Parameter getApplausedsl_parameter() {
        return applausedsl_parameter;
    }

    public void setApplausedsl_parameter(applauseDsl_Parameter applausedsl_parameter) {
        this.applausedsl_parameter = applausedsl_parameter;
    }

}