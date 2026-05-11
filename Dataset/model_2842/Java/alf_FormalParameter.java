





import java.util.List;
import java.util.ArrayList;

public class alf_FormalParameter  {

    private String direction;
    private String name;





    private alf_FormalParameterList alf_formalparameterlist;




    private alf_TypePart alf_typepart;


    public alf_FormalParameter(
        String direction,        String name    ) {
        this.direction = direction;
        this.name = name;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public alf_FormalParameterList getAlf_formalparameterlist() {
        return alf_formalparameterlist;
    }

    public void setAlf_formalparameterlist(alf_FormalParameterList alf_formalparameterlist) {
        this.alf_formalparameterlist = alf_formalparameterlist;
    }
    public alf_TypePart getAlf_typepart() {
        return alf_typepart;
    }

    public void setAlf_typepart(alf_TypePart alf_typepart) {
        this.alf_typepart = alf_typepart;
    }

}