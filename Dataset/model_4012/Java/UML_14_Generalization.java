





import java.util.List;
import java.util.ArrayList;

public class UML_14_Generalization  {

    private String discriminator;





    private UML_14_Package uml_14_package;




    private List<UML_14_Class> uml_14_classs;




    private List<UML_14_Class> uml_14_classs;


    public UML_14_Generalization(
        String discriminator    ) {
        this.discriminator = discriminator;
        this.uml_14_classs = new ArrayList<>();
        this.uml_14_classs = new ArrayList<>();
    }

    public UML_14_Generalization(
        String discriminator        ArrayList<UML_14_Class> uml_14_classs,        ArrayList<UML_14_Class> uml_14_classs    ) {
        this.discriminator = discriminator;
        this.uml_14_classs = uml_14_classs;
        this.uml_14_classs = uml_14_classs;
    }

    public String getDiscriminator() {
        return discriminator;
    }

    public void setDiscriminator(String discriminator) {
        this.discriminator = discriminator;
    }

    public UML_14_Package getUml_14_package() {
        return uml_14_package;
    }

    public void setUml_14_package(UML_14_Package uml_14_package) {
        this.uml_14_package = uml_14_package;
    }
    public List<UML_14_Class> getUml_14_classs() {
        return uml_14_classs;
    }

    public void addUml_14_class(Uml_14_class uml_14_class) {
        this.uml_14_classs.add(uml_14_class);
    }
    public List<UML_14_Class> getUml_14_classs() {
        return uml_14_classs;
    }

    public void addUml_14_class(Uml_14_class uml_14_class) {
        this.uml_14_classs.add(uml_14_class);
    }

}