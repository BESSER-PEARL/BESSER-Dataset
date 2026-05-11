





import java.util.List;
import java.util.ArrayList;

public class avm_spice_SPICEModel extends SchematicModel {

    private String Class;



    public avm_spice_SPICEModel(
        String Class    ) {
        super(
        );
        this.Class = Class;
    }


    public String getClass() {
        return Class;
    }

    public void setClass(String Class) {
        this.Class = Class;
    }


}