





import java.util.List;
import java.util.ArrayList;

public class myDsl_type_qualifier  {

    private String const;
    private String volatile;
    private String atomic;
    private String restrict;



    public myDsl_type_qualifier(
        String const,        String volatile,        String atomic,        String restrict    ) {
        this.const = const;
        this.volatile = volatile;
        this.atomic = atomic;
        this.restrict = restrict;
    }


    public String getConst() {
        return const;
    }

    public void setConst(String const) {
        this.const = const;
    }
    public String getVolatile() {
        return volatile;
    }

    public void setVolatile(String volatile) {
        this.volatile = volatile;
    }
    public String getAtomic() {
        return atomic;
    }

    public void setAtomic(String atomic) {
        this.atomic = atomic;
    }
    public String getRestrict() {
        return restrict;
    }

    public void setRestrict(String restrict) {
        this.restrict = restrict;
    }


}