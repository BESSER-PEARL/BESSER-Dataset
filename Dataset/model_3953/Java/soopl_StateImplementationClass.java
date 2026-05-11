





import java.util.List;
import java.util.ArrayList;

public class soopl_StateImplementationClass extends Class {






    private List<soopl_Method> soopl_methods;




    private soopl_StatefulClass soopl_statefulclass;




    private soopl_StateClass soopl_stateclass;


    public soopl_StateImplementationClass(
    ) {
        super(
        );
        this.soopl_methods = new ArrayList<>();
    }

    public soopl_StateImplementationClass(
        ArrayList<soopl_Method> soopl_methods    ) {
        this.soopl_methods = soopl_methods;
    }


    public List<soopl_Method> getSoopl_methods() {
        return soopl_methods;
    }

    public void addSoopl_method(Soopl_method soopl_method) {
        this.soopl_methods.add(soopl_method);
    }
    public soopl_StatefulClass getSoopl_statefulclass() {
        return soopl_statefulclass;
    }

    public void setSoopl_statefulclass(soopl_StatefulClass soopl_statefulclass) {
        this.soopl_statefulclass = soopl_statefulclass;
    }
    public soopl_StateClass getSoopl_stateclass() {
        return soopl_stateclass;
    }

    public void setSoopl_stateclass(soopl_StateClass soopl_stateclass) {
        this.soopl_stateclass = soopl_stateclass;
    }

}