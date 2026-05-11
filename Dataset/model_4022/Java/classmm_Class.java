





import java.util.List;
import java.util.ArrayList;

public class classmm_Class extends Classifier {

    private boolean isAbstract;
    private String visibility;





    private List<classmm_Method> classmm_methods;




    private classmm_Package classmm_package;




    private classmm_Attribute classmm_attribute;




    private classmm_Method classmm_method;




    private List<classmm_Attribute> classmm_attributes;




    private classmm_Class classmm_class;




    private classmm_Package classmm_package;


    public classmm_Class(
        boolean isAbstract,        String visibility    ) {
        super(
        );
        this.isAbstract = isAbstract;
        this.visibility = visibility;
        this.classmm_methods = new ArrayList<>();
        this.classmm_attributes = new ArrayList<>();
    }

    public classmm_Class(
        boolean isAbstract,        String visibility        ArrayList<classmm_Method> classmm_methods,        ArrayList<classmm_Attribute> classmm_attributes    ) {
        this.isAbstract = isAbstract;
        this.visibility = visibility;
        this.classmm_methods = classmm_methods;
        this.classmm_attributes = classmm_attributes;
    }

    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }

    public List<classmm_Method> getClassmm_methods() {
        return classmm_methods;
    }

    public void addClassmm_method(Classmm_method classmm_method) {
        this.classmm_methods.add(classmm_method);
    }
    public classmm_Package getClassmm_package() {
        return classmm_package;
    }

    public void setClassmm_package(classmm_Package classmm_package) {
        this.classmm_package = classmm_package;
    }
    public classmm_Attribute getClassmm_attribute() {
        return classmm_attribute;
    }

    public void setClassmm_attribute(classmm_Attribute classmm_attribute) {
        this.classmm_attribute = classmm_attribute;
    }
    public classmm_Method getClassmm_method() {
        return classmm_method;
    }

    public void setClassmm_method(classmm_Method classmm_method) {
        this.classmm_method = classmm_method;
    }
    public List<classmm_Attribute> getClassmm_attributes() {
        return classmm_attributes;
    }

    public void addClassmm_attribute(Classmm_attribute classmm_attribute) {
        this.classmm_attributes.add(classmm_attribute);
    }
    public classmm_Class getClassmm_class() {
        return classmm_class;
    }

    public void setClassmm_class(classmm_Class classmm_class) {
        this.classmm_class = classmm_class;
    }
    public classmm_Package getClassmm_package() {
        return classmm_package;
    }

    public void setClassmm_package(classmm_Package classmm_package) {
        this.classmm_package = classmm_package;
    }

}