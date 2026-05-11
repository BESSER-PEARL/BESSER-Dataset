





import java.util.List;
import java.util.ArrayList;

public class swrtj_Class extends Element {






    private List<swrtj_Constructor> swrtj_constructors;




    private swrtj_ConstructorInvocation swrtj_constructorinvocation;




    private List<swrtj_Interface> swrtj_interfaces;


    public swrtj_Class(
    ) {
        super(
        );
        this.swrtj_constructors = new ArrayList<>();
        this.swrtj_interfaces = new ArrayList<>();
    }

    public swrtj_Class(
        ArrayList<swrtj_Constructor> swrtj_constructors,        ArrayList<swrtj_Interface> swrtj_interfaces    ) {
        this.swrtj_constructors = swrtj_constructors;
        this.swrtj_interfaces = swrtj_interfaces;
    }


    public List<swrtj_Constructor> getSwrtj_constructors() {
        return swrtj_constructors;
    }

    public void addSwrtj_constructor(Swrtj_constructor swrtj_constructor) {
        this.swrtj_constructors.add(swrtj_constructor);
    }
    public swrtj_ConstructorInvocation getSwrtj_constructorinvocation() {
        return swrtj_constructorinvocation;
    }

    public void setSwrtj_constructorinvocation(swrtj_ConstructorInvocation swrtj_constructorinvocation) {
        this.swrtj_constructorinvocation = swrtj_constructorinvocation;
    }
    public List<swrtj_Interface> getSwrtj_interfaces() {
        return swrtj_interfaces;
    }

    public void addSwrtj_interface(Swrtj_interface swrtj_interface) {
        this.swrtj_interfaces.add(swrtj_interface);
    }

}