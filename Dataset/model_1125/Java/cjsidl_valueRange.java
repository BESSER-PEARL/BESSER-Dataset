





import java.util.List;
import java.util.ArrayList;

public class cjsidl_valueRange  {

    private String upperLimit_type;
    private String lowerLim;
    private String comment;
    private String upperLim;
    private String lowerLimit_type;





    private cjsidl_varFormatField cjsidl_varformatfield;




    private cjsidl_scopedConstId cjsidl_scopedconstid;




    private cjsidl_constReference cjsidl_constreference;




    private cjsidl_constReference cjsidl_constreference;




    private cjsidl_scopedConstId cjsidl_scopedconstid;


    public cjsidl_valueRange(
        String upperLimit_type,        String lowerLim,        String comment,        String upperLim,        String lowerLimit_type    ) {
        this.upperLimit_type = upperLimit_type;
        this.lowerLim = lowerLim;
        this.comment = comment;
        this.upperLim = upperLim;
        this.lowerLimit_type = lowerLimit_type;
    }


    public String getUpperlimit_type() {
        return upperLimit_type;
    }

    public void setUpperlimit_type(String upperLimit_type) {
        this.upperLimit_type = upperLimit_type;
    }
    public String getLowerlim() {
        return lowerLim;
    }

    public void setLowerlim(String lowerLim) {
        this.lowerLim = lowerLim;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getUpperlim() {
        return upperLim;
    }

    public void setUpperlim(String upperLim) {
        this.upperLim = upperLim;
    }
    public String getLowerlimit_type() {
        return lowerLimit_type;
    }

    public void setLowerlimit_type(String lowerLimit_type) {
        this.lowerLimit_type = lowerLimit_type;
    }

    public cjsidl_varFormatField getCjsidl_varformatfield() {
        return cjsidl_varformatfield;
    }

    public void setCjsidl_varformatfield(cjsidl_varFormatField cjsidl_varformatfield) {
        this.cjsidl_varformatfield = cjsidl_varformatfield;
    }
    public cjsidl_scopedConstId getCjsidl_scopedconstid() {
        return cjsidl_scopedconstid;
    }

    public void setCjsidl_scopedconstid(cjsidl_scopedConstId cjsidl_scopedconstid) {
        this.cjsidl_scopedconstid = cjsidl_scopedconstid;
    }
    public cjsidl_constReference getCjsidl_constreference() {
        return cjsidl_constreference;
    }

    public void setCjsidl_constreference(cjsidl_constReference cjsidl_constreference) {
        this.cjsidl_constreference = cjsidl_constreference;
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

}