





import java.util.List;
import java.util.ArrayList;

public class lSGL_Config  {

    private String name;





    private lSGL_Generator lsgl_generator;




    private lSGL_GeneratorAnnotation lsgl_generatorannotation;




    private List<lSGL_ConfigProperty> lsgl_configpropertys;


    public lSGL_Config(
        String name    ) {
        this.name = name;
        this.lsgl_configpropertys = new ArrayList<>();
    }

    public lSGL_Config(
        String name        ArrayList<lSGL_ConfigProperty> lsgl_configpropertys    ) {
        this.name = name;
        this.lsgl_configpropertys = lsgl_configpropertys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public lSGL_Generator getLsgl_generator() {
        return lsgl_generator;
    }

    public void setLsgl_generator(lSGL_Generator lsgl_generator) {
        this.lsgl_generator = lsgl_generator;
    }
    public lSGL_GeneratorAnnotation getLsgl_generatorannotation() {
        return lsgl_generatorannotation;
    }

    public void setLsgl_generatorannotation(lSGL_GeneratorAnnotation lsgl_generatorannotation) {
        this.lsgl_generatorannotation = lsgl_generatorannotation;
    }
    public List<lSGL_ConfigProperty> getLsgl_configpropertys() {
        return lsgl_configpropertys;
    }

    public void addLsgl_configproperty(Lsgl_configproperty lsgl_configproperty) {
        this.lsgl_configpropertys.add(lsgl_configproperty);
    }

}