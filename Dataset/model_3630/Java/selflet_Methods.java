





import java.util.List;
import java.util.ArrayList;

public class selflet_Methods  {






    private List<selflet_Method> selflet_methods;




    private selflet_Ability selflet_ability;


    public selflet_Methods(
    ) {
        this.selflet_methods = new ArrayList<>();
    }

    public selflet_Methods(
        ArrayList<selflet_Method> selflet_methods    ) {
        this.selflet_methods = selflet_methods;
    }


    public List<selflet_Method> getSelflet_methods() {
        return selflet_methods;
    }

    public void addSelflet_method(Selflet_method selflet_method) {
        this.selflet_methods.add(selflet_method);
    }
    public selflet_Ability getSelflet_ability() {
        return selflet_ability;
    }

    public void setSelflet_ability(selflet_Ability selflet_ability) {
        this.selflet_ability = selflet_ability;
    }

}