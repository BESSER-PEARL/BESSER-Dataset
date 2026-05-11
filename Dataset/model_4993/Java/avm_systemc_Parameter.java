





import java.util.List;
import java.util.ArrayList;

public class avm_systemc_Parameter extends DomainModelParameter {

    private String ParamPosition;
    private String ParamName;



    public avm_systemc_Parameter(
        String ParamPosition,        String ParamName    ) {
        super(
        );
        this.ParamPosition = ParamPosition;
        this.ParamName = ParamName;
    }


    public String getParamposition() {
        return ParamPosition;
    }

    public void setParamposition(String ParamPosition) {
        this.ParamPosition = ParamPosition;
    }
    public String getParamname() {
        return ParamName;
    }

    public void setParamname(String ParamName) {
        this.ParamName = ParamName;
    }


}