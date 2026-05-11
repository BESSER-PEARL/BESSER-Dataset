





import java.util.List;
import java.util.ArrayList;

public class soopl_Class extends NamedElement {

    private boolean isAbstract;





    private List<soopl_Method> soopl_methods;




    private soopl_Package soopl_package;




    private List<soopl_Property> soopl_propertys;




    private soopl_Class soopl_class;




    private soopl_ComplexTypeProperty soopl_complextypeproperty;


    public soopl_Class(
        boolean isAbstract    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.soopl_methods = new ArrayList<>();
        this.soopl_propertys = new ArrayList<>();
    }

    public soopl_Class(
        boolean isAbstract        ArrayList<soopl_Method> soopl_methods,        ArrayList<soopl_Property> soopl_propertys    ) {
        this.isAbstract = isAbstract;
        this.soopl_methods = soopl_methods;
        this.soopl_propertys = soopl_propertys;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public List<soopl_Method> getSoopl_methods() {
        return soopl_methods;
    }

    public void addSoopl_method(Soopl_method soopl_method) {
        this.soopl_methods.add(soopl_method);
    }
    public soopl_Package getSoopl_package() {
        return soopl_package;
    }

    public void setSoopl_package(soopl_Package soopl_package) {
        this.soopl_package = soopl_package;
    }
    public List<soopl_Property> getSoopl_propertys() {
        return soopl_propertys;
    }

    public void addSoopl_property(Soopl_property soopl_property) {
        this.soopl_propertys.add(soopl_property);
    }
    public soopl_Class getSoopl_class() {
        return soopl_class;
    }

    public void setSoopl_class(soopl_Class soopl_class) {
        this.soopl_class = soopl_class;
    }
    public soopl_ComplexTypeProperty getSoopl_complextypeproperty() {
        return soopl_complextypeproperty;
    }

    public void setSoopl_complextypeproperty(soopl_ComplexTypeProperty soopl_complextypeproperty) {
        this.soopl_complextypeproperty = soopl_complextypeproperty;
    }

}