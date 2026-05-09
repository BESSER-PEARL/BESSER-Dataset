





import java.util.List;
import java.util.ArrayList;

public class dsl_WildcardBounds  {

    private boolean sup;
    private boolean ext;





    private dsl_TypeArgument dsl_typeargument;




    private dsl_ReferenceType dsl_referencetype;


    public dsl_WildcardBounds(
        boolean sup,        boolean ext    ) {
        this.sup = sup;
        this.ext = ext;
    }


    public boolean getSup() {
        return sup;
    }

    public void setSup(boolean sup) {
        this.sup = sup;
    }
    public boolean getExt() {
        return ext;
    }

    public void setExt(boolean ext) {
        this.ext = ext;
    }

    public dsl_TypeArgument getDsl_typeargument() {
        return dsl_typeargument;
    }

    public void setDsl_typeargument(dsl_TypeArgument dsl_typeargument) {
        this.dsl_typeargument = dsl_typeargument;
    }
    public dsl_ReferenceType getDsl_referencetype() {
        return dsl_referencetype;
    }

    public void setDsl_referencetype(dsl_ReferenceType dsl_referencetype) {
        this.dsl_referencetype = dsl_referencetype;
    }

}