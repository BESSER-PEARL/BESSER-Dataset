





import java.util.List;
import java.util.ArrayList;

public class org_structure_PropertyAdaptationOperator extends AdaptationOperator {

    private String remover;
    private String adder;
    private String getter;
    private String setter;





    private structure_Property structure_property;


    public org_structure_PropertyAdaptationOperator(
        String remover,        String adder,        String getter,        String setter    ) {
        super(
        );
        this.remover = remover;
        this.adder = adder;
        this.getter = getter;
        this.setter = setter;
    }


    public String getRemover() {
        return remover;
    }

    public void setRemover(String remover) {
        this.remover = remover;
    }
    public String getAdder() {
        return adder;
    }

    public void setAdder(String adder) {
        this.adder = adder;
    }
    public String getGetter() {
        return getter;
    }

    public void setGetter(String getter) {
        this.getter = getter;
    }
    public String getSetter() {
        return setter;
    }

    public void setSetter(String setter) {
        this.setter = setter;
    }

    public structure_Property getStructure_property() {
        return structure_property;
    }

    public void setStructure_property(structure_Property structure_property) {
        this.structure_property = structure_property;
    }

}