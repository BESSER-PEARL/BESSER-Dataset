





import java.util.List;
import java.util.ArrayList;

public class dcmddandroid_Method extends ClassElement {

    private String returns;
    private boolean isAbstract;





    private dcmddandroid_AbstractClass dcmddandroid_abstractclass;




    private dcmddandroid_Interface dcmddandroid_interface;


    public dcmddandroid_Method(
        String returns,        boolean isAbstract    ) {
        super(
        );
        this.returns = returns;
        this.isAbstract = isAbstract;
    }


    public String getReturns() {
        return returns;
    }

    public void setReturns(String returns) {
        this.returns = returns;
    }
    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public dcmddandroid_AbstractClass getDcmddandroid_abstractclass() {
        return dcmddandroid_abstractclass;
    }

    public void setDcmddandroid_abstractclass(dcmddandroid_AbstractClass dcmddandroid_abstractclass) {
        this.dcmddandroid_abstractclass = dcmddandroid_abstractclass;
    }
    public dcmddandroid_Interface getDcmddandroid_interface() {
        return dcmddandroid_interface;
    }

    public void setDcmddandroid_interface(dcmddandroid_Interface dcmddandroid_interface) {
        this.dcmddandroid_interface = dcmddandroid_interface;
    }

}