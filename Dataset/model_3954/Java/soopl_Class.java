





import java.util.List;
import java.util.ArrayList;

public class soopl_Class extends NamedElement {

    private boolean isAbstract;





    private soopl_Package soopl_package;




    private soopl_Class soopl_class;


    public soopl_Class(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
    }


    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public soopl_Package getSoopl_package() {
        return soopl_package;
    }

    public void setSoopl_package(soopl_Package soopl_package) {
        this.soopl_package = soopl_package;
    }
    public soopl_Class getSoopl_class() {
        return soopl_class;
    }

    public void setSoopl_class(soopl_Class soopl_class) {
        this.soopl_class = soopl_class;
    }

}