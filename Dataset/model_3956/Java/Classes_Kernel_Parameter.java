





import java.util.List;
import java.util.ArrayList;

public class Classes_Kernel_Parameter extends TypedElement {

    private String default;





    private ValueSpecification valuespecification;


    public Classes_Kernel_Parameter(
        String default    ) {
        super(
        );
        this.default = default;
    }


    public String getDefault() {
        return default;
    }

    public void setDefault(String default) {
        this.default = default;
    }

    public ValueSpecification getValuespecification() {
        return valuespecification;
    }

    public void setValuespecification(ValueSpecification valuespecification) {
        this.valuespecification = valuespecification;
    }

}