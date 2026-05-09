





import java.util.List;
import java.util.ArrayList;

public class org_structure_PropertyAdaptationOperator extends AdaptationOperator {

    private String getter;
    private String adder;
    private String remover;
    private String setter;



    public org_structure_PropertyAdaptationOperator(
        String getter,        String adder,        String remover,        String setter    ) {
        super(
        );
        this.getter = getter;
        this.adder = adder;
        this.remover = remover;
        this.setter = setter;
    }


    public String getGetter() {
        return getter;
    }

    public void setGetter(String getter) {
        this.getter = getter;
    }
    public String getAdder() {
        return adder;
    }

    public void setAdder(String adder) {
        this.adder = adder;
    }
    public String getRemover() {
        return remover;
    }

    public void setRemover(String remover) {
        this.remover = remover;
    }
    public String getSetter() {
        return setter;
    }

    public void setSetter(String setter) {
        this.setter = setter;
    }


}