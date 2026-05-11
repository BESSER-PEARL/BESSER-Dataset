





import java.util.List;
import java.util.ArrayList;

public class JavaMM_Class extends Type {






    private List<JavaMM_Attribute> javamm_attributes;




    private JavaMM_Package javamm_package;


    public JavaMM_Class(
    ) {
        super(
        );
        this.javamm_attributes = new ArrayList<>();
    }

    public JavaMM_Class(
        ArrayList<JavaMM_Attribute> javamm_attributes    ) {
        this.javamm_attributes = javamm_attributes;
    }


    public List<JavaMM_Attribute> getJavamm_attributes() {
        return javamm_attributes;
    }

    public void addJavamm_attribute(Javamm_attribute javamm_attribute) {
        this.javamm_attributes.add(javamm_attribute);
    }
    public JavaMM_Package getJavamm_package() {
        return javamm_package;
    }

    public void setJavamm_package(JavaMM_Package javamm_package) {
        this.javamm_package = javamm_package;
    }

}