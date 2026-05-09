





import java.util.List;
import java.util.ArrayList;

public class cjsidl_varLenField  {

    private String upperLim;
    private String optional;
    private String name;
    private String fieldFormat;
    private String comment;
    private String countComment;
    private String lowerLim;





    private cjsidl_typeDef cjsidl_typedef;




    private cjsidl_recordDef cjsidl_recorddef;


    public cjsidl_varLenField(
        String upperLim,        String optional,        String name,        String fieldFormat,        String comment,        String countComment,        String lowerLim    ) {
        this.upperLim = upperLim;
        this.optional = optional;
        this.name = name;
        this.fieldFormat = fieldFormat;
        this.comment = comment;
        this.countComment = countComment;
        this.lowerLim = lowerLim;
    }


    public String getUpperlim() {
        return upperLim;
    }

    public void setUpperlim(String upperLim) {
        this.upperLim = upperLim;
    }
    public String getOptional() {
        return optional;
    }

    public void setOptional(String optional) {
        this.optional = optional;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFieldformat() {
        return fieldFormat;
    }

    public void setFieldformat(String fieldFormat) {
        this.fieldFormat = fieldFormat;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getCountcomment() {
        return countComment;
    }

    public void setCountcomment(String countComment) {
        this.countComment = countComment;
    }
    public String getLowerlim() {
        return lowerLim;
    }

    public void setLowerlim(String lowerLim) {
        this.lowerLim = lowerLim;
    }

    public cjsidl_typeDef getCjsidl_typedef() {
        return cjsidl_typedef;
    }

    public void setCjsidl_typedef(cjsidl_typeDef cjsidl_typedef) {
        this.cjsidl_typedef = cjsidl_typedef;
    }
    public cjsidl_recordDef getCjsidl_recorddef() {
        return cjsidl_recorddef;
    }

    public void setCjsidl_recorddef(cjsidl_recordDef cjsidl_recorddef) {
        this.cjsidl_recorddef = cjsidl_recorddef;
    }

}