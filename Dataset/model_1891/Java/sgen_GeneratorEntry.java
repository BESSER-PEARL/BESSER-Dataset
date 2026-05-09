





import java.util.List;
import java.util.ArrayList;

public class sgen_GeneratorEntry  {

    private String contentType;





    private sgen_EObject sgen_eobject;




    private sgen_GeneratorModel sgen_generatormodel;


    public sgen_GeneratorEntry(
        String contentType    ) {
        this.contentType = contentType;
    }


    public String getContenttype() {
        return contentType;
    }

    public void setContenttype(String contentType) {
        this.contentType = contentType;
    }

    public sgen_EObject getSgen_eobject() {
        return sgen_eobject;
    }

    public void setSgen_eobject(sgen_EObject sgen_eobject) {
        this.sgen_eobject = sgen_eobject;
    }
    public sgen_GeneratorModel getSgen_generatormodel() {
        return sgen_generatormodel;
    }

    public void setSgen_generatormodel(sgen_GeneratorModel sgen_generatormodel) {
        this.sgen_generatormodel = sgen_generatormodel;
    }

}