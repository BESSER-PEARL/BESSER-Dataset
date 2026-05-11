





import java.util.List;
import java.util.ArrayList;

public class henshin_text_Parameter  {

    private String name;





    private henshin_text_ModelElement henshin_text_modelelement;




    private henshin_text_ParameterType henshin_text_parametertype;




    private henshin_text_ParameterValue henshin_text_parametervalue;




    private henshin_text_Call henshin_text_call;


    public henshin_text_Parameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public henshin_text_ModelElement getHenshin_text_modelelement() {
        return henshin_text_modelelement;
    }

    public void setHenshin_text_modelelement(henshin_text_ModelElement henshin_text_modelelement) {
        this.henshin_text_modelelement = henshin_text_modelelement;
    }
    public henshin_text_ParameterType getHenshin_text_parametertype() {
        return henshin_text_parametertype;
    }

    public void setHenshin_text_parametertype(henshin_text_ParameterType henshin_text_parametertype) {
        this.henshin_text_parametertype = henshin_text_parametertype;
    }
    public henshin_text_ParameterValue getHenshin_text_parametervalue() {
        return henshin_text_parametervalue;
    }

    public void setHenshin_text_parametervalue(henshin_text_ParameterValue henshin_text_parametervalue) {
        this.henshin_text_parametervalue = henshin_text_parametervalue;
    }
    public henshin_text_Call getHenshin_text_call() {
        return henshin_text_call;
    }

    public void setHenshin_text_call(henshin_text_Call henshin_text_call) {
        this.henshin_text_call = henshin_text_call;
    }

}