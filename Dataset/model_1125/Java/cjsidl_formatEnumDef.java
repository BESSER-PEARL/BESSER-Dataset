





import java.util.List;
import java.util.ArrayList;

public class cjsidl_formatEnumDef  {

    private String index;
    private String fieldFormat;
    private String fieldFormatStr;





    private cjsidl_constReference cjsidl_constreference;




    private cjsidl_scopedConstId cjsidl_scopedconstid;




    private cjsidl_varFormatField cjsidl_varformatfield;


    public cjsidl_formatEnumDef(
        String index,        String fieldFormat,        String fieldFormatStr    ) {
        this.index = index;
        this.fieldFormat = fieldFormat;
        this.fieldFormatStr = fieldFormatStr;
    }


    public String getIndex() {
        return index;
    }

    public void setIndex(String index) {
        this.index = index;
    }
    public String getFieldformat() {
        return fieldFormat;
    }

    public void setFieldformat(String fieldFormat) {
        this.fieldFormat = fieldFormat;
    }
    public String getFieldformatstr() {
        return fieldFormatStr;
    }

    public void setFieldformatstr(String fieldFormatStr) {
        this.fieldFormatStr = fieldFormatStr;
    }

    public cjsidl_constReference getCjsidl_constreference() {
        return cjsidl_constreference;
    }

    public void setCjsidl_constreference(cjsidl_constReference cjsidl_constreference) {
        this.cjsidl_constreference = cjsidl_constreference;
    }
    public cjsidl_scopedConstId getCjsidl_scopedconstid() {
        return cjsidl_scopedconstid;
    }

    public void setCjsidl_scopedconstid(cjsidl_scopedConstId cjsidl_scopedconstid) {
        this.cjsidl_scopedconstid = cjsidl_scopedconstid;
    }
    public cjsidl_varFormatField getCjsidl_varformatfield() {
        return cjsidl_varformatfield;
    }

    public void setCjsidl_varformatfield(cjsidl_varFormatField cjsidl_varformatfield) {
        this.cjsidl_varformatfield = cjsidl_varformatfield;
    }

}