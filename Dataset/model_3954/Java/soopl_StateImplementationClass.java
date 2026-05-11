





import java.util.List;
import java.util.ArrayList;

public class soopl_StateImplementationClass extends Class {






    private soopl_StatefulClass soopl_statefulclass;




    private List<soopl_Method> soopl_methods;




    private soopl_Transition soopl_transition;


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


    public soopl_StatefulClass getSoopl_statefulclass() {
        return soopl_statefulclass;
    }

    public void setSoopl_statefulclass(soopl_StatefulClass soopl_statefulclass) {
        this.soopl_statefulclass = soopl_statefulclass;
    }
    public List<soopl_Method> getSoopl_methods() {
        return soopl_methods;
    }

    public void addSoopl_method(Soopl_method soopl_method) {
        this.soopl_methods.add(soopl_method);
    }
    public soopl_Transition getSoopl_transition() {
        return soopl_transition;
    }

    public void setSoopl_transition(soopl_Transition soopl_transition) {
        this.soopl_transition = soopl_transition;
    }

}