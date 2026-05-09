





import java.util.List;
import java.util.ArrayList;

public class cjsidl_subField  {

    private String toIndex;
    private String name;
    private String fromIndex;
    private String comment;





    private cjsidl_valueSetDef cjsidl_valuesetdef;




    private cjsidl_bitfieldDef cjsidl_bitfielddef;


    public cjsidl_subField(
        String toIndex,        String name,        String fromIndex,        String comment    ) {
        this.toIndex = toIndex;
        this.name = name;
        this.fromIndex = fromIndex;
        this.comment = comment;
    }


    public String getToindex() {
        return toIndex;
    }

    public void setToindex(String toIndex) {
        this.toIndex = toIndex;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFromindex() {
        return fromIndex;
    }

    public void setFromindex(String fromIndex) {
        this.fromIndex = fromIndex;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public cjsidl_valueSetDef getCjsidl_valuesetdef() {
        return cjsidl_valuesetdef;
    }

    public void setCjsidl_valuesetdef(cjsidl_valueSetDef cjsidl_valuesetdef) {
        this.cjsidl_valuesetdef = cjsidl_valuesetdef;
    }
    public cjsidl_bitfieldDef getCjsidl_bitfielddef() {
        return cjsidl_bitfielddef;
    }

    public void setCjsidl_bitfielddef(cjsidl_bitfieldDef cjsidl_bitfielddef) {
        this.cjsidl_bitfielddef = cjsidl_bitfielddef;
    }

}