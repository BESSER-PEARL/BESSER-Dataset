





import java.util.List;
import java.util.ArrayList;

public class vcml_VCObject  {

    private String name;





    private List<vcml_Option> vcml_options;




    private vcml_VcmlModel vcml_vcmlmodel;


    public vcml_VCObject(
        String name    ) {
        this.name = name;
        this.vcml_options = new ArrayList<>();
    }

    public vcml_VCObject(
        String name        ArrayList<vcml_Option> vcml_options    ) {
        this.name = name;
        this.vcml_options = vcml_options;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<vcml_Option> getVcml_options() {
        return vcml_options;
    }

    public void addVcml_option(Vcml_option vcml_option) {
        this.vcml_options.add(vcml_option);
    }
    public vcml_VcmlModel getVcml_vcmlmodel() {
        return vcml_vcmlmodel;
    }

    public void setVcml_vcmlmodel(vcml_VcmlModel vcml_vcmlmodel) {
        this.vcml_vcmlmodel = vcml_vcmlmodel;
    }

}