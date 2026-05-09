





import java.util.List;
import java.util.ArrayList;

public class cjsidl_taggedUnitsEnum  {

    private String fieldUnit;
    private String name;
    private String const_tag;





    private cjsidl_valueSetDef cjsidl_valuesetdef;




    private cjsidl_varField cjsidl_varfield;




    private cjsidl_scopedConstId cjsidl_scopedconstid;




    private cjsidl_simpleNumericType cjsidl_simplenumerictype;




    private cjsidl_constReference cjsidl_constreference;


    public cjsidl_taggedUnitsEnum(
        String fieldUnit,        String name,        String const_tag    ) {
        this.fieldUnit = fieldUnit;
        this.name = name;
        this.const_tag = const_tag;
    }


    public String getFieldunit() {
        return fieldUnit;
    }

    public void setFieldunit(String fieldUnit) {
        this.fieldUnit = fieldUnit;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getConst_tag() {
        return const_tag;
    }

    public void setConst_tag(String const_tag) {
        this.const_tag = const_tag;
    }

    public cjsidl_valueSetDef getCjsidl_valuesetdef() {
        return cjsidl_valuesetdef;
    }

    public void setCjsidl_valuesetdef(cjsidl_valueSetDef cjsidl_valuesetdef) {
        this.cjsidl_valuesetdef = cjsidl_valuesetdef;
    }
    public cjsidl_varField getCjsidl_varfield() {
        return cjsidl_varfield;
    }

    public void setCjsidl_varfield(cjsidl_varField cjsidl_varfield) {
        this.cjsidl_varfield = cjsidl_varfield;
    }
    public cjsidl_scopedConstId getCjsidl_scopedconstid() {
        return cjsidl_scopedconstid;
    }

    public void setCjsidl_scopedconstid(cjsidl_scopedConstId cjsidl_scopedconstid) {
        this.cjsidl_scopedconstid = cjsidl_scopedconstid;
    }
    public cjsidl_simpleNumericType getCjsidl_simplenumerictype() {
        return cjsidl_simplenumerictype;
    }

    public void setCjsidl_simplenumerictype(cjsidl_simpleNumericType cjsidl_simplenumerictype) {
        this.cjsidl_simplenumerictype = cjsidl_simplenumerictype;
    }
    public cjsidl_constReference getCjsidl_constreference() {
        return cjsidl_constreference;
    }

    public void setCjsidl_constreference(cjsidl_constReference cjsidl_constreference) {
        this.cjsidl_constreference = cjsidl_constreference;
    }

}