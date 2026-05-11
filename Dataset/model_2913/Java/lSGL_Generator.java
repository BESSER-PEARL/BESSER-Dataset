





import java.util.List;
import java.util.ArrayList;

public class lSGL_Generator  {

    private String name;





    private lSGL_Model lsgl_model;




    private lSGL_GeneratorAnnotation lsgl_generatorannotation;


    public lSGL_Generator(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public lSGL_Model getLsgl_model() {
        return lsgl_model;
    }

    public void setLsgl_model(lSGL_Model lsgl_model) {
        this.lsgl_model = lsgl_model;
    }
    public lSGL_GeneratorAnnotation getLsgl_generatorannotation() {
        return lsgl_generatorannotation;
    }

    public void setLsgl_generatorannotation(lSGL_GeneratorAnnotation lsgl_generatorannotation) {
        this.lsgl_generatorannotation = lsgl_generatorannotation;
    }

}