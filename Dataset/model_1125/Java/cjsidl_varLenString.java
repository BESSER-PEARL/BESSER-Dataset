





import java.util.List;
import java.util.ArrayList;

public class cjsidl_varLenString  {

    private String comment;
    private String lowerLim;
    private String optional;
    private String upperLim;
    private String name;





    private cjsidl_recordDef cjsidl_recorddef;




    private cjsidl_typeDef cjsidl_typedef;


    public cjsidl_varLenString(
        String comment,        String lowerLim,        String optional,        String upperLim,        String name    ) {
        this.comment = comment;
        this.lowerLim = lowerLim;
        this.optional = optional;
        this.upperLim = upperLim;
        this.name = name;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getLowerlim() {
        return lowerLim;
    }

    public void setLowerlim(String lowerLim) {
        this.lowerLim = lowerLim;
    }
    public String getOptional() {
        return optional;
    }

    public void setOptional(String optional) {
        this.optional = optional;
    }
    public String getUpperlim() {
        return upperLim;
    }

    public void setUpperlim(String upperLim) {
        this.upperLim = upperLim;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cjsidl_recordDef getCjsidl_recorddef() {
        return cjsidl_recorddef;
    }

    public void setCjsidl_recorddef(cjsidl_recordDef cjsidl_recorddef) {
        this.cjsidl_recorddef = cjsidl_recorddef;
    }
    public cjsidl_typeDef getCjsidl_typedef() {
        return cjsidl_typedef;
    }

    public void setCjsidl_typedef(cjsidl_typeDef cjsidl_typedef) {
        this.cjsidl_typedef = cjsidl_typedef;
    }

}