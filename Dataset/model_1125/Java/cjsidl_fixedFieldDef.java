





import java.util.List;
import java.util.ArrayList;

public class cjsidl_fixedFieldDef  {

    private String optional;
    private String comment;
    private String name;
    private String fieldUnit;





    private cjsidl_typeDef cjsidl_typedef;




    private cjsidl_EObject cjsidl_eobject;




    private cjsidl_recordDef cjsidl_recorddef;




    private cjsidl_simpleNumericType cjsidl_simplenumerictype;


    public cjsidl_fixedFieldDef(
        String optional,        String comment,        String name,        String fieldUnit    ) {
        this.optional = optional;
        this.comment = comment;
        this.name = name;
        this.fieldUnit = fieldUnit;
    }


    public String getOptional() {
        return optional;
    }

    public void setOptional(String optional) {
        this.optional = optional;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFieldunit() {
        return fieldUnit;
    }

    public void setFieldunit(String fieldUnit) {
        this.fieldUnit = fieldUnit;
    }

    public cjsidl_typeDef getCjsidl_typedef() {
        return cjsidl_typedef;
    }

    public void setCjsidl_typedef(cjsidl_typeDef cjsidl_typedef) {
        this.cjsidl_typedef = cjsidl_typedef;
    }
    public cjsidl_EObject getCjsidl_eobject() {
        return cjsidl_eobject;
    }

    public void setCjsidl_eobject(cjsidl_EObject cjsidl_eobject) {
        this.cjsidl_eobject = cjsidl_eobject;
    }
    public cjsidl_recordDef getCjsidl_recorddef() {
        return cjsidl_recorddef;
    }

    public void setCjsidl_recorddef(cjsidl_recordDef cjsidl_recorddef) {
        this.cjsidl_recorddef = cjsidl_recorddef;
    }
    public cjsidl_simpleNumericType getCjsidl_simplenumerictype() {
        return cjsidl_simplenumerictype;
    }

    public void setCjsidl_simplenumerictype(cjsidl_simpleNumericType cjsidl_simplenumerictype) {
        this.cjsidl_simplenumerictype = cjsidl_simplenumerictype;
    }

}