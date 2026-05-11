





import java.util.List;
import java.util.ArrayList;

public class alf_TypeName  {

    private boolean any;





    private alf_TypePart alf_typepart;




    private alf_QualifiedName alf_qualifiedname;


    public alf_TypeName(
        boolean any    ) {
        this.any = any;
    }


    public boolean getAny() {
        return any;
    }

    public void setAny(boolean any) {
        this.any = any;
    }

    public alf_TypePart getAlf_typepart() {
        return alf_typepart;
    }

    public void setAlf_typepart(alf_TypePart alf_typepart) {
        this.alf_typepart = alf_typepart;
    }
    public alf_QualifiedName getAlf_qualifiedname() {
        return alf_qualifiedname;
    }

    public void setAlf_qualifiedname(alf_QualifiedName alf_qualifiedname) {
        this.alf_qualifiedname = alf_qualifiedname;
    }

}