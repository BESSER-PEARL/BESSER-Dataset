





import java.util.List;
import java.util.ArrayList;

public class soopl_Parameter extends NamedElement {






    private soopl_CallMethodOfParameter soopl_callmethodofparameter;




    private soopl_AssignProperty soopl_assignproperty;


    public soopl_Parameter(
    ) {
        super(
        );
    }



    public soopl_CallMethodOfParameter getSoopl_callmethodofparameter() {
        return soopl_callmethodofparameter;
    }

    public void setSoopl_callmethodofparameter(soopl_CallMethodOfParameter soopl_callmethodofparameter) {
        this.soopl_callmethodofparameter = soopl_callmethodofparameter;
    }
    public soopl_AssignProperty getSoopl_assignproperty() {
        return soopl_assignproperty;
    }

    public void setSoopl_assignproperty(soopl_AssignProperty soopl_assignproperty) {
        this.soopl_assignproperty = soopl_assignproperty;
    }

}