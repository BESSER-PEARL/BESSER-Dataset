





import java.util.List;
import java.util.ArrayList;

public class aadl2_ThreadClassifier extends Thread, ComponentClassifier {






    private aadl2_ThreadSubcomponent aadl2_threadsubcomponent;


    public aadl2_ThreadClassifier(
    ) {
        super(
        );
    }



    public aadl2_ThreadSubcomponent getAadl2_threadsubcomponent() {
        return aadl2_threadsubcomponent;
    }

    public void setAadl2_threadsubcomponent(aadl2_ThreadSubcomponent aadl2_threadsubcomponent) {
        this.aadl2_threadsubcomponent = aadl2_threadsubcomponent;
    }

}