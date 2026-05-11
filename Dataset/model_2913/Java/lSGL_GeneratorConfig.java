





import java.util.List;
import java.util.ArrayList;

public class lSGL_GeneratorConfig  {

    private String values;
    private String cfgName;





    private lSGL_GeneratorAnnotation lsgl_generatorannotation;


    public lSGL_GeneratorConfig(
        String values,        String cfgName    ) {
        this.values = values;
        this.cfgName = cfgName;
    }


    public String getValues() {
        return values;
    }

    public void setValues(String values) {
        this.values = values;
    }
    public String getCfgname() {
        return cfgName;
    }

    public void setCfgname(String cfgName) {
        this.cfgName = cfgName;
    }

    public lSGL_GeneratorAnnotation getLsgl_generatorannotation() {
        return lsgl_generatorannotation;
    }

    public void setLsgl_generatorannotation(lSGL_GeneratorAnnotation lsgl_generatorannotation) {
        this.lsgl_generatorannotation = lsgl_generatorannotation;
    }

}